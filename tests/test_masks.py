import pytest

from src.masks import get_mask_card_number, get_mask_account


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
        get_mask_card_number('123card')


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'


def test_get_mask_account_wrong_number_more():
    with pytest.raises(ValueError):
        get_mask_account('7000792289606361000')


def test_get_mask_account_wrong_number_less():
    with pytest.raises(ValueError):
        get_mask_account('222')

def test_get_mask_account_not_digit():
    with pytest.raises(ValueError):
        get_mask_account('123card')