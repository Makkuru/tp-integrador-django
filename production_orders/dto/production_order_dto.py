"""DTO de exposicion para ordenes de produccion."""


class ProductionOrderDTO:
    """Define los campos publicos de una orden de produccion."""

    def __init__(self, production_order):
        self.production_order = production_order

    def to_dict(self):
        created_at = self.production_order.created_at
        return {
            'id': self.production_order.id,
            'product_name': self.production_order.product_name,
            'quantity': self.production_order.quantity,
            'status': self.production_order.status,
            'created_at': created_at.isoformat() if hasattr(created_at, 'isoformat') else created_at,
        }
