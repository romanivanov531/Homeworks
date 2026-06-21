import unittest
from collections import Counter

import pytest

from src.processing import filter_by_state, sort_by_date, search_by_keyword, count_transactions_by_category


@pytest.mark.parametrize(
    "lists_, key, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "CANCELED",
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
    ],
)
def test_filter_by_state(lists_, key, expected):
    assert filter_by_state(lists_, key) == expected


@pytest.fixture
def lists():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state_key_title(lists):
    assert filter_by_state(lists, "eXecuteD") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]

    assert filter_by_state(lists, "caNCeleD") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_by_state_wrong_key(lists):
    assert filter_by_state(lists, "bonk") == []


@pytest.mark.parametrize(
    "lists_, key, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            False,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
# Проверка правильности работы функции в целом
# Проверка учитывает разные форматы даты
def test_sort_by_date(lists_, key, expected):
    assert (
        sort_by_date(
            lists_,
            key,
        )
        == expected
    )


def test_sort_by_date_wrong_key_type(lists):
    with pytest.raises(TypeError):
        sort_by_date(lists, "True")


@pytest.fixture
def same_dates():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]

class TestSearchByKeyword(unittest.TestCase):

    def setUp(self):
        # Создаем пример списка транзакций для тестирования
        self.transactions = [
            {'description': 'покупка в магазине', 'amount': 100},
            {'description': 'платеж за услуги', 'amount': 50},
            {'description': 'покупка билетов', 'amount': 150},
            {'description': 'перевод между счетами', 'amount': 200},
        ]

    def test_search_existing_keyword(self):
        # Тест: поиск существующего ключевого слова
        result = search_by_keyword(self.transactions, 'покупка')
        expected = [
            {'description': 'покупка в магазине', 'amount': 100},
            {'description': 'покупка билетов', 'amount': 150},
        ]
        self.assertEqual(result, expected)

    def test_search_non_existing_keyword(self):
        # Тест: поиск несуществующего ключевого слова
        result = search_by_keyword(self.transactions, 'неизвестное')
        expected = []
        self.assertEqual(result, expected)

    def test_search_case_insensitivity(self):
        # Тест: поиск с учетом регистра
        result = search_by_keyword(self.transactions, 'Покупка')
        expected = [
            {'description': 'покупка в магазине', 'amount': 100},
            {'description': 'покупка билетов', 'amount': 150},
        ]
        self.assertEqual(result, expected)

    def test_search_partial_keyword(self):
        # Тест: поиск по частичному совпадению
        result = search_by_keyword(self.transactions, 'услу')
        expected = [
            {'description': 'платеж за услуги', 'amount': 50},
        ]
        self.assertEqual(result, expected)

class TestCountTransactionsByCategory(unittest.TestCase):

    def setUp(self):
        # Создаем пример списка транзакций для тестирования
        self.transactions = [
            {'description': 'покупка', 'amount': 100},
            {'description': 'платеж', 'amount': 50},
            {'description': 'покупка', 'amount': 150},
            {'description': 'перевод', 'amount': 200},
            {'description': 'платеж', 'amount': 75},
        ]

    def test_count_transactions(self):
        # Тест: подсчет транзакций по категориям
        categories = ['покупка', 'платеж', 'перевод']
        result = count_transactions_by_category(self.transactions, categories)
        expected = Counter({'покупка': 2, 'платеж': 2, 'перевод': 1})
        self.assertEqual(result, expected)

    def test_count_transactions_with_empty_list(self):
        # Тест: подсчет транзакций с пустым списком
        result = count_transactions_by_category([], ['покупка', 'платеж'])
        expected = Counter()
        self.assertEqual(result, expected)

