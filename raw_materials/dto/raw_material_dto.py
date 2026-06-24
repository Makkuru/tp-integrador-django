"""DTO de exposicion para materias primas."""


class RawMaterialDTO:
    """Define los campos publicos de una materia prima."""

    def __init__(self, raw_material):
        self.raw_material = raw_material

    def to_dict(self):
        stock_alert = self.raw_material.stock_quantity < self.raw_material.min_stock
        return {
            'id': self.raw_material.id,
            'name': self.raw_material.name,
            'unit': self.raw_material.unit,
            'stock_quantity': self.raw_material.stock_quantity,
            'min_stock': self.raw_material.min_stock,
            'stock_alert': stock_alert,
            'stock_message': 'Stock por debajo del minimo' if stock_alert else 'Stock suficiente',
        }
