"""Modelo de dominio para maquinaria."""


class Machine:
    """Representa una maquina usada por el sistema productivo."""

    STATUSES = ('OPERATIONAL', 'MAINTENANCE', 'OUT_OF_SERVICE')

    def __init__(self, id, name, type, status, last_maintenance_date):
        self.id = id
        self.name = name
        self.type = type
        self.status = status
        self.last_maintenance_date = last_maintenance_date

    def __repr__(self):
        return (
            'Machine('
            f'id={self.id}, name={self.name}, type={self.type}, '
            f'status={self.status})'
        )
