from datetime import datetime

from src import masks


def mask_account_card(number: str) -> str:
    """Функция, которая маскирует карту или номер счета"""
    mask_number = ""
    first_int_index = 0

    for item in number:
        if item.isdigit():
            first_int_index = number.index(item)
            break
    if len(number[first_int_index:]) == 16:
        mask_number += number[:first_int_index] + masks.get_mask_card_number(number[first_int_index:])
    elif len(number[first_int_index:]) == 20:
        mask_number += number[:first_int_index] + masks.get_mask_account(number[first_int_index:])
    else:
        return "Неверно введен номер"

    return mask_number


def get_date(now_date: str) -> str:
    """Функция, которая меняет формат времени по шаблону: дд.мм.гггг"""
    return datetime.strptime(now_date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")