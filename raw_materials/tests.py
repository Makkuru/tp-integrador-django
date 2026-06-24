"""Pruebas de endpoints para materias primas."""

import json

from django.test import TestCase

from raw_materials.repositories.raw_material_repository import RawMaterialRepository


class RawMaterialEndpointTests(TestCase):
    """Valida el flujo HTTP principal de materias primas."""

    def setUp(self):
        RawMaterialRepository.reset()

    def test_get_all_exposes_stock_alert(self):
        response = self.client.get('/raw-materials/')

        self.assertEqual(response.status_code, 200)
        material = next(item for item in response.json() if item['id'] == 2)
        self.assertTrue(material['stock_alert'])

    def test_create_raw_material(self):
        response = self.client.post(
            '/raw-materials/create/',
            data=json.dumps({
                'name': 'Pintura epoxi',
                'unit': 'litro',
                'stock_quantity': 25,
                'min_stock': 10,
            }),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.json()['stock_alert'])

    def test_update_stock_refreshes_alert(self):
        response = self.client.patch(
            '/raw-materials/1/stock/',
            data=json.dumps({'stock_quantity': 20}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['stock_alert'])
