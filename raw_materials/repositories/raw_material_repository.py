"""Repository en memoria para materias primas."""

from raw_materials.models.raw_material import RawMaterial


class RawMaterialRepository:
    """Unico responsable del acceso a datos de materias primas."""

    _items = [
        RawMaterial(1, 'Acero laminado', 'kg', 120, 50),
        RawMaterial(2, 'Tornillos M8', 'unidad', 35, 100),
    ]
    _next_id = 3

    @classmethod
    def reset(cls):
        """Restaura los datos iniciales para pruebas."""
        cls._items = [
            RawMaterial(1, 'Acero laminado', 'kg', 120, 50),
            RawMaterial(2, 'Tornillos M8', 'unidad', 35, 100),
        ]
        cls._next_id = 3

    def find_all(self):
        return list(self._items)

    def find_by_id(self, entity_id):
        return next((item for item in self._items if item.id == entity_id), None)

    def save(self, raw_material):
        if raw_material.id is None:
            raw_material.id = self.__class__._next_id
            self.__class__._next_id += 1
            self.__class__._items.append(raw_material)
            return raw_material

        existing = self.find_by_id(raw_material.id)
        if existing is None:
            self.__class__._items.append(raw_material)
            return raw_material

        index = self.__class__._items.index(existing)
        self.__class__._items[index] = raw_material
        return raw_material

    def delete(self, entity_id):
        item = self.find_by_id(entity_id)
        if item is None:
            return None
        self.__class__._items.remove(item)
        return item
