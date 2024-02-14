import json
from cl.category import Category
from cl.product import Product


def load_products_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        categories = []
        for category_data in data:
            category = Category(category_data["name"], category_data["description"])
            for product_data in category_data["products"]:
                product = Product(product_data["name"], product_data["description"], product_data["price"],
                                  product_data["quantity"])
                category.products.append(product)
            categories.append(category)
    return categories


# Пример использования:
categories = load_products_from_json('products.json')
for category in categories:
    print(f"Название: {category.name}, Описание: {category.description}")
    for product in category.products:
        print(
            f"Название: {product.name}, Описание: {product.description}, Цена: {product.price}, "
            f"Количество в наличии: {product.quantity}")
