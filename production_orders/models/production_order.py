"""Modelo de dominio para ordenes de produccion."""

from datetime import datetime, timezone


class ProductionOrder:
    """Representa una orden de produccion dentro del dominio ERP."""

    STATUSES = ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED')

    def __init__(self, id, product_name, quantity, status='PENDING', created_at=None):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity
        self.status = status
        self.created_at = created_at or datetime.now(timezone.utc)

    def __repr__(self):
        return (
            'ProductionOrder('
            f'id={self.id}, product_name={self.product_name}, '
            f'quantity={self.quantity}, status={self.status})'
        )
