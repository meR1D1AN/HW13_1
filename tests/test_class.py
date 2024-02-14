from utils.hw_class import Category, Product


def test_category_initialization():
    category = Category("Тест категории", "Тест описания")
    assert category.name == "Тест категории"
    assert category.description == "Тест описания"


def test_product_initialization():
    product = Product("Тест названия", "Тест описания", 100, 10)
    assert product.name == "Тест названия"
    assert product.description == "Тест описания"
    assert product.price == 10
    assert product.quantity == 100


def test_unique_products_count():
    initial_unique_count = len(Category.total_unique_products)
    product1 = Product("Тест Продукта 1", "Описание 1", 15, 10.0)
    product2 = Product("Тест Продукта 2", "Описание 1", 8, 13.0)
    assert len(Category.total_unique_products) - initial_unique_count == 2


def test_total_categories_count():
    initial_categories_count = Category.total_categories
    category1 = Category("Категория 1", "Описание 1")
    category2 = Category("Категория 2", "Описание 2")
    assert Category.total_categories - initial_categories_count == 2
