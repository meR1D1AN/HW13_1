class Product:
    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def get_product_name(self):
        return self.name

    def get_description(self):
        return self.description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        elif new_price < self._price:
            confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() == "y":
                self._price = new_price
                print("Цена успешно понижена")
            else:
                print("Действие отменено")
        else:
            self._price = new_price

    def get_quantity(self):
        return self.quantity

    @classmethod
    def create_product(cls, name, description, price, quantity, product_list):
        for product in product_list:
            if product.name == name:
                if product.price > price:
                    product.quantity += quantity
                else:
                    product.price = price
                    product.quantity = quantity
                return
        return cls(name, description, price, quantity)
