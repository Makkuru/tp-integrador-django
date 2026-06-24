"""DTO de exposicion para maquinaria."""


class MachineDTO:
    """Define los campos publicos de una maquina."""

    def __init__(self, machine):
        self.machine = machine

    def to_dict(self):
        return {
            'id': self.machine.id,
            'name': self.machine.name,
            'type': self.machine.type,
            'status': self.machine.status,
            'last_maintenance_date': self.machine.last_maintenance_date,
        }
