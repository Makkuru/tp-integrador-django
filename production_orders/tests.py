"""Pruebas de endpoints para ordenes de produccion."""

import json

from django.test import TestCase

from production_orders.repositories.production_order_repository import ProductionOrderRepository


class ProductionOrderEndpointTests(TestCase):
    """Valida el flujo HTTP principal de ordenes de produccion."""

    def setUp(self):
        ProductionOrderRepository.reset()

    def test_get_all_returns_orders(self):
        response = self.client.get('/production-orders/')

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 2)

    def test_create_order_defaults_to_pending(self):
        response = self.client.post(
            '/production-orders/create/',
            data=json.dumps({'product_name': 'Banco de trabajo', 'quantity': 4}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'PENDING')

    def test_change_status_updates_order(self):
        response = self.client.patch(
            '/production-orders/1/status/',
            data=json.dumps({'status': 'COMPLETED'}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'COMPLETED')

    def test_missing_order_returns_404(self):
        response = self.client.get('/production-orders/999/')

        self.assertEqual(response.status_code, 404)
