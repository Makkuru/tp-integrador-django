"""Excepciones de dominio para operarios."""


class OperatorException(Exception):
    """Representa un error de negocio de operarios."""

    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class OperatorNotFoundException(OperatorException):
    """Informa que un operario no existe."""

    def __init__(self, entity_id):
        super().__init__(
            message=f'Recurso con ID {entity_id} no encontrado.',
            status_code=404,
        )
