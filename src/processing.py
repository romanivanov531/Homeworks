def filter_by_state(list_: list[dict], key: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state.
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    filtered_list = []
    for item in list_:
        if item.get("state") == key:
            filtered_list.append(item)
        else:
            continue
    return filtered_list


def sort_by_date(list_: list[dict], route: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Возвращает список, отсортированный по ключу date """
    return sorted(list_, key=lambda x: x["date"], reverse=route)
