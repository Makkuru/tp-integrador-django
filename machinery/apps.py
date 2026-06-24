"""Configuracion de la app machinery."""

from django.apps import AppConfig


class MachineryConfig(AppConfig):
    """Declara la configuracion Django de maquinaria."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'machinery'
