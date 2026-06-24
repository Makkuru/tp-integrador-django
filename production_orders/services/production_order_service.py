"""Service de negocio para ordenes de produccion."""

from production_orders.dto.production_order_dto import ProductionOrderDTO
from production_orders.exceptions.production_order_exception import ProductionOrderNotFoundException
from production_orders.models.production_order import ProductionOrder
from production_orders.repositories.production_order_repository import ProductionOrderRepository
from production_orders.validators.production_order_validator import ProductionOrderValidator


class ProductionOrderService:
    """Contiene reglas de negocio de ordenes de produccion."""

    def __init__(self):
        self.repository = ProductionOrderRepository()

    def get_all(self):
        return [ProductionOrderDTO(item) for item in self.repository.find_all()]

    def get_by_id(self, order_id):
        item = self.repository.find_by_id(order_id)
        if item is None:
            raise ProductionOrderNotFoundException(order_id)
        return ProductionOrderDTO(item)

    def create(self, data):
        ProductionOrderValidator.validate_create(data)
        item = ProductionOrder(
            id=None,
            product_name=data['product_name'],
            quantity=int(data['quantity']),
            status=data.get('status', 'PENDING'),
        )
        return ProductionOrderDTO(self.repository.save(item))

    def change_status(self, order_id, status):
        ProductionOrderValidator.validate_status(status)
        item = self.repository.find_by_id(order_id)
        if item is None:
            raise ProductionOrderNotFoundException(order_id)
        item.status = status
        return ProductionOrderDTO(self.repository.save(item))
