from cl.category import Category
from cl.product import Product


def test_category_initialization():
    category = Category("Тест названия", "Тест описания")
    assert category.name == "Тест названия"
    assert category.description == "Тест описания"
    assert category.products == []


def test_product_initialization():
    product = Product("Тест названия", "Тест описания", 500.0, 10)
    assert product.name == "Тест названия"
    assert product.description == "Тест описания"
    assert product.quantity == 500.0
    assert product.price == 10


def test_count_products():
    initial_unique_products_count = Category.total_unique_products
    product1 = Product("Тест Продукта 1", "Описание 1", 500.0, 10)
    product2 = Product("Тест Продукта 1", "Описание 2", 1000.0, 5)
    assert Category.total_unique_products == initial_unique_products_count + 2


def test_count_categories():
    initial_categories_count = Category.total_categories
    category1 = Category("Категория 1", "Описание 1")
    category2 = Category("Категория 2", "Описание 2")
    assert Category.total_categories == initial_categories_count + 2


def test_add_product_to_category():
    category = Category("Тест категории", "Тест описания категории")
    product = Product("Тест продукта", "Тест описания продукта", 500.0, 10)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
