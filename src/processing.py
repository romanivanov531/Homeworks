import re
from collections import Counter


def filter_by_state(list_: list[dict], key: str = 'EXECUTED') -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state.
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    filtered_list = []
    upper_key = key.upper()

    for item in list_:
        if item.get('state') == upper_key:
            filtered_list.append(item)
        else:
            continue
    return filtered_list


def sort_by_date(list_: list[dict], route: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает список, отсортированный по ключу date """
    if not isinstance(route, bool):
        raise TypeError('Неверный тип данных')

    return sorted(list_, key=lambda x: x["date"], reverse=route)


def search_by_keyword(info: list, search: str) -> list:
  '''Функция для фильтрации списка транзакций по ключевому слову в описании'''
    normal_search = search.lower()
    return [operation for operation in info if re.search(normal_search, operation.get('description').lower())]


def count_transactions_by_category(transactions: list, categories: list) -> dict:
   '''Функция для фильтрации списка транзакций по ключевым словам в описании'''
    counted = Counter(i.get('description') for i in transactions)
    return counted
