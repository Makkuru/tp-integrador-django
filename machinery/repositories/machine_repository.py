"""Repository en memoria para maquinaria."""

from machinery.models.machine import Machine


class MachineRepository:
    """Unico responsable del acceso a datos de maquinaria."""

    _items = [
        Machine(1, 'Cortadora laser', 'Corte', 'OPERATIONAL', '2026-05-12'),
        Machine(2, 'Prensa hidraulica', 'Prensado', 'MAINTENANCE', '2026-06-10'),
    ]
    _next_id = 3

    @classmethod
    def reset(cls):
        """Restaura los datos iniciales para pruebas."""
        cls._items = [
            Machine(1, 'Cortadora laser', 'Corte', 'OPERATIONAL', '2026-05-12'),
            Machine(2, 'Prensa hidraulica', 'Prensado', 'MAINTENANCE', '2026-06-10'),
        ]
        cls._next_id = 3

    def find_all(self):
        return list(self._items)

    def find_by_id(self, entity_id):
        return next((item for item in self._items if item.id == entity_id), None)

    def save(self, machine):
        existing = self.find_by_id(machine.id)
        if existing is None:
            if machine.id is None:
                machine.id = self.__class__._next_id
                self.__class__._next_id += 1
            self.__class__._items.append(machine)
            return machine

        index = self.__class__._items.index(existing)
        self.__class__._items[index] = machine
        return machine

    def delete(self, entity_id):
        item = self.find_by_id(entity_id)
        if item is None:
            return None
        self.__class__._items.remove(item)
        return item
