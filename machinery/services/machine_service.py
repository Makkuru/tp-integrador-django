"""Service de negocio para maquinaria."""

from machinery.dto.machine_dto import MachineDTO
from machinery.exceptions.machine_exception import MachineNotFoundException
from machinery.repositories.machine_repository import MachineRepository
from machinery.validators.machine_validator import MachineValidator


class MachineService:
    """Contiene reglas de negocio de maquinaria."""

    def __init__(self):
        self.repository = MachineRepository()

    def get_all(self):
        return [MachineDTO(item) for item in self.repository.find_all()]

    def get_by_id(self, machine_id):
        item = self.repository.find_by_id(machine_id)
        if item is None:
            raise MachineNotFoundException(machine_id)
        return MachineDTO(item)

    def change_status(self, machine_id, status):
        MachineValidator.validate_status(status)
        item = self.repository.find_by_id(machine_id)
        if item is None:
            raise MachineNotFoundException(machine_id)
        item.status = status
        return MachineDTO(self.repository.save(item))
