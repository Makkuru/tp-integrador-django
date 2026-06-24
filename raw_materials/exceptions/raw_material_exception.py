"""Excepciones de dominio para materias primas."""


class RawMaterialException(Exception):
    """Representa un error de negocio de materias primas."""

    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class RawMaterialNotFoundException(RawMaterialException):
    """Informa que una materia prima no existe."""

    def __init__(self, entity_id):
        super().__init__(
            message=f'Recurso con ID {entity_id} no encontrado.',
            status_code=404,
        )
