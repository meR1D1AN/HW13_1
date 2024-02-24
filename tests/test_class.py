from cl.category import Category
from cl.product import Product
from utils.load_json import load_data
import os


def test_product_str():
    product = Product("Товар", "Описание", 100.0, 10)
    assert str(product) == 'Товар, 100.0 руб. Остаток: 10 шт.'


def test_product_add():
    product1 = Product("Товар", "Описание", 100.0, 10)
    product2 = Product("Товар", "Описание", 200.0, 5)
    total_quantity = product1 + product2
    assert total_quantity == 2000


def test_product_setter():
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0


def test_product_create():
    product_list = [Product("Товар", "Описание", 100.0, 10)]
    product = Product.create_product("Товар", "Описание", 200.0, 5, product_list)
    assert len(product_list) == 1


def test_category_len():
    products = [Product("Товар1", "Описание1", 100.0, 10),
                Product("Товар2", "Описание2", 200.0, 5)]
    category = Category("Тест названия категории", "Тест описания категории", products)
    assert len(category) == 15


def test_category_str():
    products = [Product("Товар1", "Описание1", 100.0, 10),
                Product("Товар2", "Описание2", 200.0, 5)]
    category = Category("Тест названия категории", "Тест описания категории", products)
    assert str(category) == "Тест названия категории, количество продуктов, 15 шт."


def test_category_add_product():
    category = Category("Тест названия категории", "Тест описания категории", [])
    product = Product("Товар", "Описание", 100.0, 10)
    category.add_product(product)
    assert len(category.products_) == 1


def test_category_remove_product():
    category = Category("Тест названия категории", "Тест описания категории", [])
    product = Product("Товар", "Описание", 100.0, 10)
    category.remove_product(product)
    assert len(category.products_) == 0


def test_category_initialization():
    category = Category("Тест названия категории", "Тест описания категории", {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    })
    assert category.name == "Тест названия категории"
    assert category.description == "Тест описания категории"
    assert category.products_ == {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    }
    assert category.name_ == "Тест названия категории"
    assert category.description_ == "Тест описания категории"
    assert category.products_ == {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    }


def test_product_initialization():
    product = Product("Тест названия товара", "Тест описания товара", 500.0, 10)
    assert product.name == "Тест названия товара"
    assert product.description == "Тест описания товара"
    assert product._price == 500.0
    assert product.quantity == 10

    assert product.name_ == "Тест названия товара"
    assert product.description_ == "Тест описания товара"
    assert product.price == 500.0
    assert product.quantity_ == 10


def test_load_data_list():
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_abs_path = os.path.join(current_dir, "utils", "products.json")

    assert os.path.isfile(file_abs_path)
    data = load_data()
    assert isinstance(data, list)
