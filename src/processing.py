def filter_by_state(list_: list, key: str = 'EXECUTED') -> list:
    filtered_list = []
    for item in list_:
        if item.get('state') == key:
            filtered_list.append(item)
        else:
            continue
    return filtered_list

def sort_by_date(list_: list, route:bool = True) -> list:
    return sorted(list_, key=lambda x: x.get('date'), reverse=route)
