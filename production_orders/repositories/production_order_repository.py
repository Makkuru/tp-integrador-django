"""Repository en memoria para ordenes de produccion."""

from production_orders.models.production_order import ProductionOrder


class ProductionOrderRepository:
    """Unico responsable del acceso a datos de ordenes de produccion."""

    _items = [
        ProductionOrder(1, 'Mesa metalica', 20, 'PENDING'),
        ProductionOrder(2, 'Gabinete industrial', 8, 'IN_PROGRESS'),
    ]
    _next_id = 3

    @classmethod
    def reset(cls):
        """Restaura los datos iniciales para pruebas."""
        cls._items = [
            ProductionOrder(1, 'Mesa metalica', 20, 'PENDING'),
            ProductionOrder(2, 'Gabinete industrial', 8, 'IN_PROGRESS'),
        ]
        cls._next_id = 3

    def find_all(self):
        return list(self._items)

    def find_by_id(self, entity_id):
        return next((item for item in self._items if item.id == entity_id), None)

    def save(self, production_order):
        if production_order.id is None:
            production_order.id = self.__class__._next_id
            self.__class__._next_id += 1
            self.__class__._items.append(production_order)
            return production_order

        existing = self.find_by_id(production_order.id)
        if existing is None:
            self.__class__._items.append(production_order)
            return production_order

        index = self.__class__._items.index(existing)
        self.__class__._items[index] = production_order
        return production_order

    def delete(self, entity_id):
        item = self.find_by_id(entity_id)
        if item is None:
            return None
        self.__class__._items.remove(item)
        return item
