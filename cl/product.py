from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def name_(self):
        pass

    @property
    @abstractmethod
    def description_(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @property
    @abstractmethod
    def quantity_(self):
        pass

    @abstractmethod
    def create_product(self, name, description, price, quantity, color, product_list):
        pass


class Mixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"Создан объект: {self.__class__.__name__}\n\t{self.__dict__.items()}"


class Product(AbstractProduct, Mixin):
    name: str
    description: str
    _price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return f'{self.name}, {self._price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
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

    @staticmethod
    def create_product(name, description, price, quantity, color, product_list):
        for product in product_list:
            if (product.name == name and
                    product.description == description and
                    product.price == price and
                    product.quantity == quantity and
                    product.color == color):
                if product.price < price:
                    product.price = price
                product.quantity += quantity
                return product
        new_product = Product(name, description, price, quantity, color)
        product_list.append(new_product)
        return new_product


class Smartphone(Product, Mixin):
    def __init__(self, name, description, price, quantity, color, perfomance, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.perfomance = perfomance
        self.model = model
        self.memory = memory

    def __str__(self):
        return (f'{self.color} {self.name} {self.model}, {self.memory} ГБ, {self.perfomance} Ггц.\n'
                f'Цена: {self.price} руб. Остаток: {self.quantity} шт.\n'
                f'Описание: {self.description}\n')


class LawnGrass(Product, Mixin):
    def __init__(self, name, description, price, quantity, color, manufacturing_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.manufacturing_country = manufacturing_country
        self.germination_period = germination_period

    def __str__(self):
        return (f'{self.name}, Цвет: {self.color}.\n'
                f'Страна: {self.manufacturing_country}.\n'
                f'Цена: {self.price} руб. и Остаток: {self.quantity} шт.\n'
                f'Описание: {self.description}\n'
                f'Срок прорастания: {self.germination_period} дней.\n')
