class Product:
    """
    Representa un producto del dominio.
    """

    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price
        