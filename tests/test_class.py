from cl.category import Category
from cl.product import Product
import pytest
import os
from utils.load_json import load_data


#
#
def test_category_initialization():
    category = Category("Тест названия категории", "Тест описания категории", {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    })
    assert category.name == "Тест названия категории"
    assert category.description == "Тест описания категории"
    assert category.products == {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    }

    assert category.get_name() == "Тест названия категории"
    assert category.get_description() == "Тест описания категории"
    assert category.get_products() == {
        "name": "Тест названия товара",
        "description": "Тест описания товара",
        "price": 180000.0,
        "quantity": 5
    }

    assert category.total_categories == 1
    assert category.total_unique_products == 0


def test_product_initialization():
    product = Product("Тест названия товара", "Тест описания товара", 500.0, 10)
    assert product.name == "Тест названия товара"
    assert product.description == "Тест описания товара"
    assert product.price == 500.0
    assert product.quantity == 10

    assert product.get_product_name() == "Тест названия товара"
    assert product.get_description() == "Тест описания товара"
    assert product.get_price() == 500.0
    assert product.get_quantity() == 10


def test_load_data_list():
    data = load_data()
    assert isinstance(data, list)


def test_load_data():
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_abs_path = os.path.join(current_dir, "utils", "products.json")

    assert os.path.isfile(file_abs_path)

    data = load_data()
    assert isinstance(data, list)
