"""Modelo de dominio para lineas de produccion."""


class ProductionLine:
    """Representa una linea productiva asociada a maquina y operario."""

    STATUSES = ('ACTIVE', 'INACTIVE')

    def __init__(self, id, name, machine_id, operator_id, status='INACTIVE'):
        self.id = id
        self.name = name
        self.machine_id = machine_id
        self.operator_id = operator_id
        self.status = status

    def __repr__(self):
        return (
            'ProductionLine('
            f'id={self.id}, name={self.name}, machine_id={self.machine_id}, '
            f'operator_id={self.operator_id}, status={self.status})'
        )
