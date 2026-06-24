"""Configuracion de la app production_lines."""

from django.apps import AppConfig


class ProductionLinesConfig(AppConfig):
    """Declara la configuracion Django de lineas de produccion."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'production_lines'
