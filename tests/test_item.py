from src.item import Item

import pytest

@pytest.fixture
def items():
    return Item("Samsung", 50000, 2)

def test_calculate_total_price(items):
    assert items.calculate_total_price() == 100000


def test_apply_discount(items):
    assert items.apply_discount() == 50000
