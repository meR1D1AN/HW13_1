from cl.category import Category
from cl.product import Product, Smartphone, LawnGrass
from utils.load_json import load_data
import os
import pytest


def test_product_str():
    product = Product("Товар", "Описание", 100.0, 10, "red")
    assert str(product) == 'Товар, 100.0 руб. Остаток: 10 шт.'


def test_add_product_valid():
    category = Category("test category", "test description", [])
    product = Product("test product", "test description", 10.0, 5, "red")
    category.add_product(product)
    assert product in category.products_


def test_add_product_invalid_type():
    category = Category("test category", "test description", [])
    invalid_product = "not a product"
    with pytest.raises(TypeError):
        category.add_product(invalid_product)


def test_remove_product_valid():
    product = Product("test product", "test description", 10.0, 5, "red")
    category = Category("test category", "test description", [product])
    category.remove_product(product)
    assert product not in category.products_


def test_remove_product_invalid_type():
    category = Category("test category", "test description", [])
    invalid_product = "not a product"
    with pytest.raises(TypeError):
        category.remove_product(invalid_product)


def test_product_setter():
    product = Product("Товар", "Описание", 100.0, 10, "red")
    product.price = 200.0
    assert product.price == 200.0


def test_create_product():
    product_list = []
    # создаем первый продукт
    product1 = Product.create_product("name1", "description1", 10, 20, "color1", product_list)
    assert product1 in product_list

    # обновляем существующий продукт
    product2 = Product.create_product("name1", "description1", 15, 30, "color1", product_list)
    assert product2 in product_list
    assert product2.price == 15
    assert product2.quantity == 30

    # создаем новый продукт
    product3 = Product.create_product("name2", "description2", 20, 40, "color2", product_list)
    assert product3 in product_list
    assert len(product_list) == 3


def test_category_len():
    products = [Product("Товар1", "Описание1", 100.0, 10, "red"),
                Product("Товар2", "Описание2", 200.0, 5, "blue")]
    category = Category("Тест названия категории", "Тест описания категории", products)
    assert len(category) == 15


def test_category_str():
    products = [Product("Товар1", "Описание1", 100.0, 10, "red"),
                Product("Товар2", "Описание2", 200.0, 5, "blue")]
    category = Category("Тест названия категории", "Тест описания категории", products)
    assert str(category) == "Тест названия категории, количество продуктов, 15 шт."


def test_category_add_product():
    category = Category("Тест названия категории", "Тест описания категории", [])
    product = Product("Товар", "Описание", 100.0, 10, "red")
    category.add_product(product)
    assert len(category.products_) == 1


def test_category_remove_product():
    category = Category("Тест названия категории", "Тест описания категории", [])
    product = Product("Товар", "Описание", 100.0, 10, "red")
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
    product = Product("Тест названия товара", "Тест описания товара", 500.0, 10,
                      "red")
    assert product.name == "Тест названия товара"
    assert product.description == "Тест описания товара"
    assert product._price == 500.0
    assert product.quantity == 10
    assert product.color == "red"

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


def test_smartphone_str():
    smartphone = Smartphone("iPhone", "Best smartphone", 1000, 10, "black",
                            "high", "X", 256)
    expected_output = "black iPhone X, 256 ГБ, high Ггц.\nЦена: 1000 руб. Остаток: 10 шт.\nОписание: Best smartphone\n"
    assert str(smartphone) == expected_output


# test_lawn_grass.py

def test_lawn_grass_str():
    lawn_grass = LawnGrass("Green grass", "Best grass", 5, 100, "green",
                           "USA", "2 weeks")
    expected_output = ("Green grass, Цвет: green.\nСтрана: USA.\nЦена: 5 руб. и Остаток: 100 шт.\n"
                       "Описание: Best grass\nСрок прорастания: 2 weeks дней.\n")
    assert str(lawn_grass) == expected_output


def test_product_add_():
    product1 = Product("Product1", "Description1", 10, 5, "red")
    product2 = Product("Product2", "Description2", 20, 3, "blue")
    expected_total_quantity = (10 * 5) + (20 * 3)
    assert (product1 + product2) == expected_total_quantity


def test_product_price_setter_lower():
    product = Product("Product1", "Description1", 10, 5, "red")
    product.price = 8
    assert product.price == 8


def test_product_price_setter_same():
    product = Product("Товар1", "Описание1", 10, 5, "red")
    product.price = 10
    assert product.price == 10


def test_product_price_setter_invalid():
    product = Product("Товар1", "Описание1", 10, 5, "red")
    product.price = -5
    assert product.price == 10
