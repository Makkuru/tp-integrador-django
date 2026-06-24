"""Validadores de entrada para operarios."""


class OperatorValidator:
    """Verifica integridad de datos antes de procesarlos."""

    @staticmethod
    def validate_create(data):
        for field in ('name', 'last_name', 'role'):
            if not data.get(field):
                raise ValueError(f'El campo {field} es obligatorio.')
        if 'is_active' in data and not isinstance(data['is_active'], bool):
            raise ValueError('El campo is_active debe ser booleano.')
