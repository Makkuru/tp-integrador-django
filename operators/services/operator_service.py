"""Service de negocio para operarios."""

from operators.dto.operator_dto import OperatorDTO
from operators.exceptions.operator_exception import OperatorNotFoundException
from operators.models.operator import Operator
from operators.repositories.operator_repository import OperatorRepository
from operators.validators.operator_validator import OperatorValidator


class OperatorService:
    """Contiene reglas de negocio de operarios."""

    def __init__(self):
        self.repository = OperatorRepository()

    def get_all(self):
        return [OperatorDTO(item) for item in self.repository.find_all()]

    def get_by_id(self, operator_id):
        item = self.repository.find_by_id(operator_id)
        if item is None:
            raise OperatorNotFoundException(operator_id)
        return OperatorDTO(item)

    def create(self, data):
        OperatorValidator.validate_create(data)
        item = Operator(
            id=None,
            name=data['name'],
            last_name=data['last_name'],
            role=data['role'],
            is_active=bool(data.get('is_active', True)),
        )
        return OperatorDTO(self.repository.save(item))

    def set_active(self, operator_id, is_active):
        item = self.repository.find_by_id(operator_id)
        if item is None:
            raise OperatorNotFoundException(operator_id)
        item.is_active = is_active
        return OperatorDTO(self.repository.save(item))
