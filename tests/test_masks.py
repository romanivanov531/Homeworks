import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_number, expected', [
    ('1596837868705199', '1596 83** **** 5199'),
    ('7158300734726758', '7158 30** **** 6758'),
    ('6831982476737658', '6831 98** **** 7658')
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_wrong_number_more():
    with pytest.raises(ValueError):
        get_mask_card_number('7000792289606361000')


def test_get_mask_card_number_wrong_number_less():
    with pytest.raises(ValueError):
        get_mask_card_number('222')

def test_get_mask_card_number_not_digit():
    with pytest.raises(ValueError):
        get_mask_card_number('123card')

@pytest.mark.parametrize('acc_number, expected', [
    ('73654108430135874305', '**4305'),
    ('35383033474447895560', '**5560'),
    ('64686473678894779589', '**9589')
])
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected


def test_get_mask_account_wrong_number_more():
    with pytest.raises(ValueError):
        get_mask_account('7000792289606361000')


def test_get_mask_account_wrong_number_less():
    with pytest.raises(ValueError):
        get_mask_account('')

def test_get_mask_account_not_digit():
    with pytest.raises(ValueError):
        get_mask_account('123card')


def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account(73654108430135874305)