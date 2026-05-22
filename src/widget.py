from datetime import datetime

from src import masks


def mask_account_card(number: str) -> str:
    """Функция, которая маскирует карту или номер счета"""
    mask_number = ""
    first_int_index = None

    if not isinstance(number, str):
        raise TypeError('Неверный тип данных')

    clean_number = number.replace(' ', '')
    for item in clean_number:
        if item.isdigit():
            first_int_index = clean_number.index(item)
            break

    if len(clean_number[first_int_index:]) == 16:
        mask_number += clean_number[:first_int_index] + ' ' + masks.get_mask_card_number(clean_number[first_int_index:])

    elif len(clean_number[first_int_index:]) == 20:
        mask_number += clean_number[:first_int_index] + ' ' + masks.get_mask_account(clean_number[first_int_index:])

    else:
        raise ValueError('Некорректный номер')

    return mask_number


def get_date(now_date: str) -> str:
    """Функция, которая меняет формат времени по шаблону: дд.мм.гггг"""
    try:
        return datetime.strptime(now_date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError('Некорректный формат даты, ожидается ISO формат')


print(mask_account_card(123))