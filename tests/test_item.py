"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


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

def test_third_homework(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'

def test_fourth_homework():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    
def test_sixth_homework():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
