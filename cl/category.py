class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []  # Инициализируем список продуктов для каждой категории
        Category.total_categories += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            Category.total_unique_products += 1
