class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, ):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            Category.total_unique_products += 1