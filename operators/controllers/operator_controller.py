"""Controller HTTP para operarios."""

import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from operators.exceptions.operator_exception import OperatorException
from operators.services.operator_service import OperatorService

logger = logging.getLogger(__name__)


class OperatorController:
    """Recibe peticiones HTTP de operarios y responde en JSON."""

    def __init__(self):
        self.service = OperatorService()

    def get_all(self, request):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /operators/ - inicio')
        try:
            items = self.service.get_all()
            data = [item.to_dict() for item in items]
            logger.info('GET /operators/ - %s registros', len(data))
            return JsonResponse(data, safe=False, status=200)
        except Exception as exc:
            logger.error('Error en get_all: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    def get_by_id(self, request, operator_id):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /operators/%s/ - inicio', operator_id)
        try:
            item = self.service.get_by_id(operator_id)
            return JsonResponse(item.to_dict(), status=200)
        except OperatorException as exc:
            logger.warning('Error de dominio en get_by_id: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en get_by_id: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def create(self, request):
        if request.method != 'POST':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /operators/create/ - inicio')
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
            item = self.service.create(payload)
            return JsonResponse(item.to_dict(), status=201)
        except (ValueError, OperatorException) as exc:
            message = getattr(exc, 'message', str(exc))
            status_code = getattr(exc, 'status_code', 400)
            logger.warning('Error de validacion en create: %s', message)
            return JsonResponse({'error': message}, status=status_code)
        except json.JSONDecodeError:
            logger.warning('JSON invalido en create')
            return JsonResponse({'error': 'JSON invalido'}, status=400)
        except Exception as exc:
            logger.error('Error en create: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def activate(self, request, operator_id):
        if request.method not in ('POST', 'PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /operators/%s/activate/ - inicio', operator_id)
        try:
            item = self.service.set_active(operator_id, True)
            return JsonResponse(item.to_dict(), status=200)
        except OperatorException as exc:
            logger.warning('Error de dominio en activate: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en activate: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def deactivate(self, request, operator_id):
        if request.method not in ('POST', 'PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /operators/%s/deactivate/ - inicio', operator_id)
        try:
            item = self.service.set_active(operator_id, False)
            return JsonResponse(item.to_dict(), status=200)
        except OperatorException as exc:
            logger.warning('Error de dominio en deactivate: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en deactivate: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
