from cl.category import Category
from cl.product import Product

import pytest


def test_category_initialization():
    category = Category("Тест категории", "Тест описания")
    assert category.name == "Тест категории"
    assert category.description == "Тест описания"


def test_product_initialization():
    product = Product("Smartphone", "Latest model", 500.0, 10)
    assert product.name == "Smartphone"
    assert product.description == "Latest model"
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
