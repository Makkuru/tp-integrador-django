"""Controller HTTP para lineas de produccion."""

import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from production_lines.exceptions.production_line_exception import ProductionLineException
from production_lines.services.production_line_service import ProductionLineService

logger = logging.getLogger(__name__)


class ProductionLineController:
    """Recibe peticiones HTTP de lineas de produccion y responde en JSON."""

    def __init__(self):
        self.service = ProductionLineService()

    def get_all(self, request):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /production-lines/ - inicio')
        try:
            items = self.service.get_all()
            data = [item.to_dict() for item in items]
            logger.info('GET /production-lines/ - %s registros', len(data))
            return JsonResponse(data, safe=False, status=200)
        except Exception as exc:
            logger.error('Error en get_all: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    def get_by_id(self, request, line_id):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /production-lines/%s/ - inicio', line_id)
        try:
            item = self.service.get_by_id(line_id)
            return JsonResponse(item.to_dict(), status=200)
        except ProductionLineException as exc:
            logger.warning('Error de dominio en get_by_id: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en get_by_id: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def activate(self, request, line_id):
        if request.method not in ('POST', 'PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /production-lines/%s/activate/ - inicio', line_id)
        try:
            item = self.service.activate(line_id)
            return JsonResponse(item.to_dict(), status=200)
        except ProductionLineException as exc:
            logger.warning('Error de dominio en activate: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en activate: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def deactivate(self, request, line_id):
        if request.method not in ('POST', 'PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /production-lines/%s/deactivate/ - inicio', line_id)
        try:
            item = self.service.deactivate(line_id)
            return JsonResponse(item.to_dict(), status=200)
        except ProductionLineException as exc:
            logger.warning('Error de dominio en deactivate: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en deactivate: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
