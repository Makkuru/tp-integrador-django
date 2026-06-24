"""Modelo de dominio para operarios."""


class Operator:
    """Representa un operario asignable a procesos productivos."""

    def __init__(self, id, name, last_name, role, is_active=True):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.role = role
        self.is_active = is_active

    def __repr__(self):
        return (
            'Operator('
            f'id={self.id}, name={self.name}, last_name={self.last_name}, '
            f'role={self.role}, is_active={self.is_active})'
        )
