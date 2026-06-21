import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('number, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected
    assert mask_account_card(number) == expected


@pytest.fixture
def date():
    return '2024-03-11T02:26:18.671407'


def test_get_date(date):
    assert get_date(date) == '11.03.2024'


def test_get_date_wrong_format():
    with pytest.raises(ValueError):
        get_date('11.03.24')


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date('')
