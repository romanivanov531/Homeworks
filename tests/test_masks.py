import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


def test_get_mask_card_number_wrong_number_more():
    with pytest.raises(ValueError):
        get_mask_card_number('7000792289606361000')


def test_get_mask_card_number_wrong_number_less():
    with pytest.raises(ValueError):
        get_mask_card_number('222')

def test_get_mask_card_number_not_digit():
    with pytest.raises(ValueError):
        get_mask_card_number('card')