import json
import logging
import os

if not os.path.isdir('../logs'):
    os.mkdir('../logs')

path = '../logs'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s] %(module)10s:%(lineno)d %(levelname)7s - %(message)s',
                    filemode='a',
                    filename=os.path.join(path, 'utils.log'))


def take_operations_info(directory: str) -> list:
    '''Функция для чтения JSON файлов'''
    logger.debug('Начало работы - take_operations_info')

    try:
        logger.info('Открытие файла по указанной директории')
        with open(f'{directory}', 'r') as file:
            logger.info('Загрузка данных из файла JSON и преобразование в объект Python.')
            operations_info = json.load(file)
            logger.debug('Конец работы - take_operations_info')
        return list(operations_info)
    except Exception as e:
        logger.error(e)
        print(e)
        return []
