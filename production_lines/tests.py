"""Pruebas de endpoints para lineas de produccion."""

from django.test import TestCase

from machinery.repositories.machine_repository import MachineRepository
from production_lines.repositories.production_line_repository import ProductionLineRepository


class ProductionLineEndpointTests(TestCase):
    """Valida el flujo HTTP principal de lineas de produccion."""

    def setUp(self):
        MachineRepository.reset()
        ProductionLineRepository.reset()

    def test_activate_line_with_operational_machine(self):
        response = self.client.post('/production-lines/1/activate/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ACTIVE')

    def test_cannot_activate_line_with_machine_in_maintenance(self):
        response = self.client.post('/production-lines/2/activate/')

        self.assertEqual(response.status_code, 409)

    def test_deactivate_line(self):
        self.client.post('/production-lines/1/activate/')

        response = self.client.post('/production-lines/1/deactivate/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'INACTIVE')
