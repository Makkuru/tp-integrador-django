"""Repository en memoria para lineas de produccion."""

from production_lines.models.production_line import ProductionLine


class ProductionLineRepository:
    """Unico responsable del acceso a datos de lineas de produccion."""

    _items = [
        ProductionLine(1, 'Linea de corte', 1, 1, 'INACTIVE'),
        ProductionLine(2, 'Linea de prensado', 2, 2, 'INACTIVE'),
    ]
    _next_id = 3

    @classmethod
    def reset(cls):
        """Restaura los datos iniciales para pruebas."""
        cls._items = [
            ProductionLine(1, 'Linea de corte', 1, 1, 'INACTIVE'),
            ProductionLine(2, 'Linea de prensado', 2, 2, 'INACTIVE'),
        ]
        cls._next_id = 3

    def find_all(self):
        return list(self._items)

    def find_by_id(self, entity_id):
        return next((item for item in self._items if item.id == entity_id), None)

    def save(self, production_line):
        existing = self.find_by_id(production_line.id)
        if existing is None:
            if production_line.id is None:
                production_line.id = self.__class__._next_id
                self.__class__._next_id += 1
            self.__class__._items.append(production_line)
            return production_line

        index = self.__class__._items.index(existing)
        self.__class__._items[index] = production_line
        return production_line

    def delete(self, entity_id):
        item = self.find_by_id(entity_id)
        if item is None:
            return None
        self.__class__._items.remove(item)
        return item
