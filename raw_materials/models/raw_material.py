"""Modelo de dominio para materias primas."""


class RawMaterial:
    """Representa una materia prima usada en produccion."""

    def __init__(self, id, name, unit, stock_quantity, min_stock):
        self.id = id
        self.name = name
        self.unit = unit
        self.stock_quantity = stock_quantity
        self.min_stock = min_stock

    def __repr__(self):
        return (
            'RawMaterial('
            f'id={self.id}, name={self.name}, unit={self.unit}, '
            f'stock_quantity={self.stock_quantity}, min_stock={self.min_stock})'
        )
