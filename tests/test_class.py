from cl.category import Category
from cl.product import Product


#
#
def test_category_initialization():
    category = Category("Тест названия", "Тест описания")
    assert category.name == "Тест названия"
    assert category.description == "Тест описания"
    assert category.products == []

    assert category.get_name() == "Тест названия"
    assert category.get_description() == "Тест описания"
    assert category.get_products() == []

    assert category.total_categories == 1
    assert category.total_unique_products == 0


def test_product_initialization():
    product = Product("Тест названия", "Тест описания", 500.0, 10)
    assert product.name == "Тест названия"
    assert product.description == "Тест описания"
    assert product.price == 500.0
    assert product.quantity == 10

    assert product.get_product_name() == "Тест названия"
    assert product.get_description() == "Тест описания"
    assert product.get_price() == 500.0
    assert product.get_quantity() == 10
