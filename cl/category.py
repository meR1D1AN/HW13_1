class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1

    @property
    def products(self):
        return self.__products

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.__products

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
            Category.total_unique_products += 1

    def display_products(self):
        for product in self.__products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
