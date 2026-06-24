"""Pruebas de endpoints para operarios."""

import json

from django.test import TestCase

from operators.repositories.operator_repository import OperatorRepository


class OperatorEndpointTests(TestCase):
    """Valida el flujo HTTP principal de operarios."""

    def setUp(self):
        OperatorRepository.reset()

    def test_get_by_id_returns_operator(self):
        response = self.client.get('/operators/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['last_name'], 'Uria')

    def test_create_operator(self):
        response = self.client.post(
            '/operators/create/',
            data=json.dumps({
                'name': 'Joaquin',
                'last_name': 'Perez',
                'role': 'Tecnico de mantenimiento',
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()['is_active'])

    def test_deactivate_operator(self):
        response = self.client.post('/operators/1/deactivate/')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['is_active'])
