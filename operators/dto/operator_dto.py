"""DTO de exposicion para operarios."""


class OperatorDTO:
    """Define los campos publicos de un operario."""

    def __init__(self, operator):
        self.operator = operator

    def to_dict(self):
        return {
            'id': self.operator.id,
            'name': self.operator.name,
            'last_name': self.operator.last_name,
            'role': self.operator.role,
            'is_active': self.operator.is_active,
        }
