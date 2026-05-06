def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты
    в формате XXXX XX** **** XXXX"""
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция, которая маскирует номер счёта
    в формате **XXXX"""
    mask_account = "**" + account[-4:]
    return mask_account
