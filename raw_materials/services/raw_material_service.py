"""Service de negocio para materias primas."""

from raw_materials.dto.raw_material_dto import RawMaterialDTO
from raw_materials.exceptions.raw_material_exception import RawMaterialNotFoundException
from raw_materials.models.raw_material import RawMaterial
from raw_materials.repositories.raw_material_repository import RawMaterialRepository
from raw_materials.validators.raw_material_validator import RawMaterialValidator


class RawMaterialService:
    """Contiene reglas de negocio de materias primas."""

    def __init__(self):
        self.repository = RawMaterialRepository()

    def get_all(self):
        return [RawMaterialDTO(item) for item in self.repository.find_all()]

    def get_by_id(self, material_id):
        item = self.repository.find_by_id(material_id)
        if item is None:
            raise RawMaterialNotFoundException(material_id)
        return RawMaterialDTO(item)

    def create(self, data):
        RawMaterialValidator.validate_create(data)
        item = RawMaterial(
            id=None,
            name=data['name'],
            unit=data['unit'],
            stock_quantity=float(data['stock_quantity']),
            min_stock=float(data['min_stock']),
        )
        return RawMaterialDTO(self.repository.save(item))

    def update_stock(self, material_id, stock_quantity):
        RawMaterialValidator.validate_stock_quantity(stock_quantity)
        item = self.repository.find_by_id(material_id)
        if item is None:
            raise RawMaterialNotFoundException(material_id)
        item.stock_quantity = float(stock_quantity)
        return RawMaterialDTO(self.repository.save(item))
