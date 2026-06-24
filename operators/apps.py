"""Configuracion de la app operators."""

from django.apps import AppConfig


class OperatorsConfig(AppConfig):
    """Declara la configuracion Django de operarios."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'operators'
