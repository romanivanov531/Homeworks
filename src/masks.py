import logging
import os

if not os.path.isdir('../logs'):
    os.mkdir('../logs')

path = '../logs/'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s] %(module)10s:%(lineno)d %(levelname)7s - %(message)s',
                    filemode='a',
                    filename=os.path.join(path, 'masks.log'))


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты
    в формате XXXX XX** **** XXXX"""
    logger.debug('Начало работы - get_mask_card_number')

    logger.info('Проверка типа данных - str')
    if not isinstance(card_number, str):
        logger.error('Неверный тип данных')
        raise TypeError('Неверный тип данных')

    logger.info('Проверка соответствия длины номера карты - 16')
    if len(card_number) > 16 or len(card_number) < 16:
        logger.error('Неверная длина номера карты')
        raise ValueError('Неверно введен номер')

    logger.info('Проверка: все ли символы являются цифрами')
    if not card_number.isdigit():
        logger.error('Неверно введен номер')
        raise ValueError('Неверно введен номер')

    logger.info('Маскировка номера карты')
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    logger.debug('Конец работы - get_mask_card_number')
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция, которая маскирует номер счёта
    в формате **XXXX"""
    logger.debug('Начала работы - get_mask_account')

    logger.info('Проверка входящих типов данных - str')
    if not isinstance(account, str):
        logger.error('Неверный тип данных')
        raise TypeError('Неверный тип данных')

    logger.info('Проверка длины номера - 20')
    if len(account) > 20 or len(account) < 20:
        logger.error(f'Неверная длина номера: {len(account)} != 20')
        raise ValueError('Неверно введен номер')

    logger.info('Проверка: все знаки являются цифрами')
    if not account.isdigit():
        logger.error('Неверно введен номер')
        raise ValueError('Неверно введен номер')

    logger.info('Маскировка номера счета')
    mask_account = "**" + account[-4:]
    logger.debug('Конец работы  - get_mask_account')
    return mask_account
