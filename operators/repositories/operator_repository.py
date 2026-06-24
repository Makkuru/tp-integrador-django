"""Repository en memoria para operarios."""

from operators.models.operator import Operator


class OperatorRepository:
    """Unico responsable del acceso a datos de operarios."""

    _items = [
        Operator(1, 'Emanuel', 'Uria', 'Supervisor de produccion', True),
        Operator(2, 'Mariana', 'Gomez', 'Operaria de linea', False),
    ]
    _next_id = 3

    @classmethod
    def reset(cls):
        """Restaura los datos iniciales para pruebas."""
        cls._items = [
            Operator(1, 'Emanuel', 'Uria', 'Supervisor de produccion', True),
            Operator(2, 'Mariana', 'Gomez', 'Operaria de linea', False),
        ]
        cls._next_id = 3

    def find_all(self):
        return list(self._items)

    def find_by_id(self, entity_id):
        return next((item for item in self._items if item.id == entity_id), None)

    def save(self, operator):
        if operator.id is None:
            operator.id = self.__class__._next_id
            self.__class__._next_id += 1
            self.__class__._items.append(operator)
            return operator

        existing = self.find_by_id(operator.id)
        if existing is None:
            self.__class__._items.append(operator)
            return operator

        index = self.__class__._items.index(existing)
        self.__class__._items[index] = operator
        return operator

    def delete(self, entity_id):
        item = self.find_by_id(entity_id)
        if item is None:
            return None
        self.__class__._items.remove(item)
        return item
