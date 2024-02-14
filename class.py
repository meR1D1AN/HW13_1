class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []


class Product:
    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
