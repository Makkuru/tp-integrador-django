"""Controller HTTP para maquinaria."""

import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from machinery.exceptions.machine_exception import MachineException
from machinery.services.machine_service import MachineService

logger = logging.getLogger(__name__)


class MachineController:
    """Recibe peticiones HTTP de maquinaria y responde en JSON."""

    def __init__(self):
        self.service = MachineService()

    def get_all(self, request):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /machinery/ - inicio')
        try:
            items = self.service.get_all()
            data = [item.to_dict() for item in items]
            logger.info('GET /machinery/ - %s registros', len(data))
            return JsonResponse(data, safe=False, status=200)
        except Exception as exc:
            logger.error('Error en get_all: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    def get_by_id(self, request, machine_id):
        if request.method != 'GET':
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('GET /machinery/%s/ - inicio', machine_id)
        try:
            item = self.service.get_by_id(machine_id)
            return JsonResponse(item.to_dict(), status=200)
        except MachineException as exc:
            logger.warning('Error de dominio en get_by_id: %s', exc.message)
            return JsonResponse({'error': exc.message}, status=exc.status_code)
        except Exception as exc:
            logger.error('Error en get_by_id: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    @csrf_exempt
    def change_status(self, request, machine_id):
        if request.method not in ('PATCH', 'PUT'):
            return JsonResponse({'error': 'Metodo no permitido'}, status=405)
        logger.info('PATCH /machinery/%s/status/ - inicio', machine_id)
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
            item = self.service.change_status(machine_id, payload.get('status'))
            return JsonResponse(item.to_dict(), status=200)
        except (ValueError, MachineException) as exc:
            message = getattr(exc, 'message', str(exc))
            status_code = getattr(exc, 'status_code', 400)
            logger.warning('Error de dominio en change_status: %s', message)
            return JsonResponse({'error': message}, status=status_code)
        except json.JSONDecodeError:
            logger.warning('JSON invalido en change_status')
            return JsonResponse({'error': 'JSON invalido'}, status=400)
        except Exception as exc:
            logger.error('Error en change_status: %s', str(exc))
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
