"""Excepciones de dominio para lineas de produccion."""


class ProductionLineException(Exception):
    """Representa un error de negocio de lineas de produccion."""

    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class ProductionLineNotFoundException(ProductionLineException):
    """Informa que una linea de produccion no existe."""

    def __init__(self, entity_id):
        super().__init__(
            message=f'Recurso con ID {entity_id} no encontrado.',
            status_code=404,
        )
