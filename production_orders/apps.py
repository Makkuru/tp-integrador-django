"""Configuracion de la app production_orders."""

from django.apps import AppConfig


class ProductionOrdersConfig(AppConfig):
    """Declara la configuracion Django de ordenes de produccion."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'production_orders'
