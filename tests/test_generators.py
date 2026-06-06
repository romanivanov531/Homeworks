import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, usd_check, rub_check):
    result_usd = filter_by_currency(transactions, "USD")
    result_rub = filter_by_currency(transactions, "RUB")
    assert list(result_usd) == usd_check
    assert list(result_rub) == rub_check


def test_filter_by_currency_wrong_key(transactions):
    result_eur = filter_by_currency(transactions, "EUR")
    assert list(result_eur) == []


def test_filter_by_currency_empty_input():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions, descriptions_list):
    description = transaction_descriptions(transactions)
    assert list(description) == descriptions_list


def test_transaction_descriptions_empty_input():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_numbers_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected


def test_card_numbers_generator_value_input():
    with pytest.raises(ValueError):
        list(card_number_generator(2, 1))

    min_difference_start = card_number_generator(1, 1)
    assert list(min_difference_start) == ["0000 0000 0000 0001"]

    min_difference_stop = card_number_generator(9999999999999999, 9999999999999999)
    assert list(min_difference_stop) == ["9999 9999 9999 9999"]
