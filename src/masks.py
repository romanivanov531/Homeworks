def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты
    в формате XXXX XX** **** XXXX"""
    if not isinstance(card_number, str):
        raise TypeError('Неверный тип данных')

    if len(card_number) > 16 or len(card_number) < 16:
        raise ValueError('Неверно введен номер')

    if not card_number.isdigit():
        raise ValueError('Неверно введен номер')

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция, которая маскирует номер счёта
    в формате **XXXX"""
    if not isinstance(account, str):
        raise TypeError('Неверный тип данных')

    if len(account) > 20 or len(account) < 20:
        raise ValueError('Неверно введен номер')

    if not account.isdigit():
        raise ValueError('Неверно введен номер')

    mask_account = "**" + account[-4:]
    return mask_account
