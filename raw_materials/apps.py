"""Configuracion de la app raw_materials."""

from django.apps import AppConfig


class RawMaterialsConfig(AppConfig):
    """Declara la configuracion Django de materias primas."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'raw_materials'
