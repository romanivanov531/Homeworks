def filter_by_state(list_: list, key: str = 'EXECUTED') -> list:
    filtered_list = []
    for item in list_:
        if item.get('state') == key:
            filtered_list.append(item)
        else:
            continue
    return filtered_list

