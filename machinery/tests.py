"""Pruebas de endpoints para maquinaria."""

import json

from django.test import TestCase

from machinery.repositories.machine_repository import MachineRepository


class MachineEndpointTests(TestCase):
    """Valida el flujo HTTP principal de maquinaria."""

    def setUp(self):
        MachineRepository.reset()

    def test_get_all_returns_machines(self):
        response = self.client.get('/machinery/')

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 2)

    def test_change_status_updates_machine(self):
        response = self.client.patch(
            '/machinery/1/status/',
            data=json.dumps({'status': 'MAINTENANCE'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'MAINTENANCE')

    def test_invalid_status_returns_400(self):
        response = self.client.patch(
            '/machinery/1/status/',
            data=json.dumps({'status': 'BROKEN'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
