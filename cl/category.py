from cl.product import Product


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

    def __str__(self):
        total_quantity = len(self)
        return f"{self.name}, количество продуктов, {total_quantity} шт."

    def __len__(self):
        return sum(product.quantity for product in self.__products)

    @property
    def name_(self):
        return self.name

    @property
    def description_(self):
        return self.description

    @property
    def products_(self):
        return self.__products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты и их наследников")
        if product not in self.__products:
            self.__products.append(product)
            Category.total_unique_products += 1

    def remove_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно удалять только продукты и их наследников")
        if product in self.__products:
            self.__products.remove(product)
            Category.total_unique_products -= 1

    def calculate_avg_price(self):
        total_price = sum(product.price * product.quantity for product in self.__products)
        total_quantity = sum(product.quantity for product in self.__products)

        try:
            avg_price = total_price / total_quantity
        except ZeroDivisionError:
            return 0

        return avg_price
