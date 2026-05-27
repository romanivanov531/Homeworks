from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable:
    ''' Декоратор для логирования деталей выполнения функций.
        Записывает данные: Имя функции, время выполнения, результат, исключения.
        При наличии аргумента записывает данные в файл filename.
        При отсутствии аргумента выводит данные в консоль.'''
    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start = datetime.strftime(datetime.now(), '%d/%m/%y %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(f'{filename}.txt', 'a', encoding='utf-8') as file:
                        file.write(f'Start:{start}  {func.__name__}  result:{result}\n')

                else:
                    print(f'Start:{start}  {func.__name__}  result:{result}')

            except Exception as e:
                if filename:
                    with open(f'{filename}.txt', 'a', encoding='utf-8') as file:
                        file.write(f'Start:{start}  {func.__name__}  Error:{e}  input:{args}  {kwargs}\n')
                else:
                    print(f'Start:{start}  {func.__name__}  Error:{e}  input:{args}  {kwargs}\n')
                raise ValueError('ff')

            return result
        return inner
    return wrapper
