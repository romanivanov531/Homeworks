import json


def take_operations_info(directory: str) -> list:
    '''Функция для чтения JSON файлов'''
    try:
        with open(f'{directory}', 'r') as file:
            operations_info = json.load(file)
        return list(operations_info)
    except Exception as e:
        print(e)
        return []
