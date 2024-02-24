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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        total_quantity = (self.price * self.quantity) + (other.price * other.quantity)
        return total_quantity

    @property
    def name_(self):
        return self.name

    @property
    def description_(self):
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

    @property
    def quantity_(self):
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
