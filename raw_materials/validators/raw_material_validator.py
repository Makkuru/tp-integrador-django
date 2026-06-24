"""Validadores de entrada para materias primas."""


class RawMaterialValidator:
    """Verifica integridad de datos antes de procesarlos."""

    @staticmethod
    def validate_create(data):
        for field in ('name', 'unit', 'stock_quantity', 'min_stock'):
            if field not in data or data[field] in (None, ''):
                raise ValueError(f'El campo {field} es obligatorio.')
        RawMaterialValidator.validate_stock_quantity(data['stock_quantity'])
        RawMaterialValidator.validate_min_stock(data['min_stock'])

    @staticmethod
    def validate_stock_quantity(value):
        try:
            stock_quantity = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError('El campo stock_quantity debe ser numerico.') from exc
        if stock_quantity < 0:
            raise ValueError('El campo stock_quantity no puede ser negativo.')

    @staticmethod
    def validate_min_stock(value):
        try:
            min_stock = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError('El campo min_stock debe ser numerico.') from exc
        if min_stock < 0:
            raise ValueError('El campo min_stock no puede ser negativo.')
