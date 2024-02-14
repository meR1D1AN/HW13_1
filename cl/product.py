from cl.category import Category


class Product:
    name: str
    description: str
    price: float
    quantity: str

    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_unique_products += 1
