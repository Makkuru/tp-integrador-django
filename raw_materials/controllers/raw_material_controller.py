"""Controller HTTP para materias primas."""

import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from raw_materials.exceptions.raw_material_exception import RawMaterialException
from raw_materials.services.raw_material_service import RawMaterialService

logger = logging.getLogger(__name__)


class RawMaterialController:
    """Recibe peticiones HTTP de materias primas y responde en JSON."""

    def __init__(self):
        self.service = RawMaterialService()

    def get_all(self, request):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /raw-materials/ - inicio')
        try:
            items = self.service.get_all()
            data = [item.to_dict() for item in items]
            logger.info('GET /raw-materials/ - %s registros', len(data))
            return JsonResponse(data, safe=False, status=200)
        except Exception as exc:
            logger.error('Error en get_all: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    def get_by_id(self, request, material_id):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /raw-materials/%s/ - inicio', material_id)
        try:
            item = self.service.get_by_id(material_id)
            return JsonResponse(item.to_dict(), status=200)
        except RawMaterialException as exc:
            logger.warning('Error de dominio en get_by_id: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en get_by_id: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def create(self, request):
        if request.method != 'POST':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('POST /raw-materials/create/ - inicio')
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
            item = self.service.create(payload)
            return JsonResponse(item.to_dict(), status=201)
        except (ValueError, RawMaterialException) as exc:
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
    def update_stock(self, request, material_id):
        if request.method not in ('PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('PATCH /raw-materials/%s/stock/ - inicio', material_id)
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
            item = self.service.update_stock(material_id, payload.get('stock_quantity'))
            return JsonResponse(item.to_dict(), status=200)
        except (ValueError, RawMaterialException) as exc:
            message = getattr(exc, 'message', str(exc))
            status_code = getattr(exc, 'status_code', 400)
            logger.warning('Error de dominio en update_stock: %s', message)
            return JsonResponse({'error': message}, status=status_code)
        except json.JSONDecodeError:
            logger.warning('JSON invalido en update_stock')
            return JsonResponse({'error': 'JSON invalido'}, status=400)
        except Exception as exc:
            logger.error('Error en update_stock: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
