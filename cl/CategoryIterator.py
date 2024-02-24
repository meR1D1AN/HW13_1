from cl.category import Category
from cl.product import Product


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            current_product = self.category.products[self.index]
            self.index += 1
            return current_product
        raise StopIteration
