from cl.category import Category
from cl.product import Product
from cl.CategoryIterator import CategoryIterator
from utils.load_json import load_data


def main():
    data = load_data()
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'],
                              product_data['quantity'])
            products.append(product)

        category = Category(category_data['name'], category_data['description'], products)
        categories.append(category)

        Category.total_unique_products += len(products)

    print_categories_and_products(categories)

    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего уникальных продуктов: {Category.total_unique_products}")


def print_categories_and_products(categories):
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print("Товары:")
        for product in category.products_:
            print(f"\tИмя товара: {product.name}")
            print(f"\tОписание товара: {product.description}")
            print(f"\tЦена: {product._price}")
            print(f"\tКол-во: {product.quantity}")
            print()


if __name__ == "__main__":
    main()
