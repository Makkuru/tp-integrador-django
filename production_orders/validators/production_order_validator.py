"""Validadores de entrada para ordenes de produccion."""

from production_orders.models.production_order import ProductionOrder


class ProductionOrderValidator:
    """Verifica integridad de datos antes de procesarlos."""

    @staticmethod
    def validate_create(data):
        if not data.get('product_name'):
            raise ValueError('El campo product_name es obligatorio.')
        if 'quantity' not in data:
            raise ValueError('El campo quantity es obligatorio.')
        try:
            quantity = int(data['quantity'])
        except (TypeError, ValueError) as exc:
            raise ValueError('El campo quantity debe ser un numero entero.') from exc
        if quantity <= 0:
            raise ValueError('El campo quantity debe ser mayor a cero.')
        if data.get('status') is not None:
            ProductionOrderValidator.validate_status(data['status'])

    @staticmethod
    def validate_status(status):
        if status not in ProductionOrder.STATUSES:
            valid = ', '.join(ProductionOrder.STATUSES)
            raise ValueError(f'Estado invalido. Estados permitidos: {valid}.')
