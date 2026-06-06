from typing import Any, Dict, Generator, List


def filter_by_currency(my_list: List[Dict[str, Any]], key: str = 'USD') -> Generator[Dict[str, Any]]:
    '''Функция принимает список транзакций в виде словарей и фильтрует по валюте.
    По умолчанию валюта USD.
    '''
    for item in my_list:
        if item['operationAmount']['currency']['code'] == key:
            yield item


def transaction_descriptions(my_list: list[Dict[str, Any]]) -> Generator[str]:
    '''Функция принимает список транзакций в виде словарей и возвращает описание каждой операции по очереди.'''
    for a in my_list:
        description = a['description']
        yield description


def card_number_generator(start: int, stop: int) -> Generator:
    '''Генератор, который выдает номера карт в формате: ХХХХ ХХХХ ХХХХ ХХХХ.
    Генератор работает в диапазоне от 0000 0000 0000 0000 до 9999 9999 9999 9999.
    Для генерации необходимы граничные значения.
    '''
    if start < 1 or stop > 9999999999999999 or stop < start:
        raise ValueError('Нарушено одно из правил:'
                         'Начальное значение меньше 1'
                         'Конечное значение больше 999999999999'
                         'Начальное значение больше конечного')
    for number in range(start, stop + 1):
        new_number = f'{number:016d}'
        new_card = new_number[:4] + ' ' + new_number[5:9] + ' ' + new_number[9:13] + ' ' + new_number[12:]
        yield new_card
