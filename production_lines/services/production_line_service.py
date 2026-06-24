"""Service de negocio para lineas de produccion."""

from machinery.repositories.machine_repository import MachineRepository
from production_lines.dto.production_line_dto import ProductionLineDTO
from production_lines.exceptions.production_line_exception import (
    ProductionLineException,
    ProductionLineNotFoundException,
)
from production_lines.repositories.production_line_repository import ProductionLineRepository


class ProductionLineService:
    """Contiene reglas de negocio de lineas de produccion."""

    def __init__(self):
        self.repository = ProductionLineRepository()
        self.machine_repository = MachineRepository()

    def get_all(self):
        return [ProductionLineDTO(item) for item in self.repository.find_all()]

    def get_by_id(self, line_id):
        item = self.repository.find_by_id(line_id)
        if item is None:
            raise ProductionLineNotFoundException(line_id)
        return ProductionLineDTO(item)

    def activate(self, line_id):
        item = self.repository.find_by_id(line_id)
        if item is None:
            raise ProductionLineNotFoundException(line_id)

        machine = self.machine_repository.find_by_id(item.machine_id)
        if machine is None:
            raise ProductionLineException('La maquina asociada no existe.', status_code=400)
        if machine.status == 'MAINTENANCE':
            raise ProductionLineException(
                'No se puede activar una linea con maquinaria en mantenimiento.',
                status_code=409,
            )

        item.status = 'ACTIVE'
        return ProductionLineDTO(self.repository.save(item))

    def deactivate(self, line_id):
        item = self.repository.find_by_id(line_id)
        if item is None:
            raise ProductionLineNotFoundException(line_id)
        item.status = 'INACTIVE'
        return ProductionLineDTO(self.repository.save(item))
