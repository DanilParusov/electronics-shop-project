"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_first_homework(item):
    assert item.calculate_total_price() == 200000
    item.apply_discount()
    assert item.price == 10000

def test_second_homework(item):
    assert item.name == "Смартфон"
    item.name = 'Телефон'
    assert item.name == 'Телефон'


    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5

    Item.instantiate_from_csv()
    assert len(Item.all) == 5