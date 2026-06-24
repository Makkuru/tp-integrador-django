"""DTO de exposicion para lineas de produccion."""


class ProductionLineDTO:
    """Define los campos publicos de una linea de produccion."""

    def __init__(self, production_line):
        self.production_line = production_line

    def to_dict(self):
        return {
            'id': self.production_line.id,
            'name': self.production_line.name,
            'machine_id': self.production_line.machine_id,
            'operator_id': self.production_line.operator_id,
            'status': self.production_line.status,
        }
