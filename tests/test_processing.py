import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('lists_, key, expected', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
     'EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
     'CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}])
])


def test_filter_by_state(lists_, key, expected):
    assert filter_by_state(lists_, key) == expected


@pytest.fixture
def lists():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]


def test_filter_by_state_key_title(lists):
    assert filter_by_state(lists,'eXecuteD') == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

    assert filter_by_state(lists, 'caNCeleD') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]


def test_filter_by_state_wrong_key(lists):
    assert filter_by_state(lists, 'bonk') == []


@pytest.mark.parametrize('lists_, key, expected', [
    (
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'}],
     True , [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'}]
    ),
    (
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
     False , [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    )
    ]
        )
# Проверка правильности работы функции в целом
# Проверка учитывает разные форматы даты
def test_sort_by_date(lists_, key, expected):
    assert sort_by_date(lists_, key,) == expected


def test_sort_by_date_wrong_key_type(lists):
    with pytest.raises(TypeError):
        sort_by_date(lists, 'True')


@pytest.fixture
def same_dates():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_same_date(same_dates):
    sort_by_date(same_dates, True) == same_dates
