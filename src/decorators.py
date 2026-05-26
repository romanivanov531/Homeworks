from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable:
    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename:
                try:
                    now = datetime.now()
                    start = now.strftime('%d/%m/%Y %H:%M:%S')
                    result = func(*args, **kwargs)
                    with open(f'{filename}', 'a', encoding='utf-8') as file:
                        file.write(f'Time:{start}  {func.__name__}   Result:{result}\n')
                except Exception as e:
                    now = datetime.now()
                    start = now.strftime('%d/%m/%Y %H:%M:%S')
                    with open(f'{filename}', 'a', encoding='utf-8') as file:
                        file.write(f'Time:{start}  {func.__name__}  Error:{e}  Input: {args}\n')
                    raise ValueError(e)
                return result
            else:
                try:
                    result = func(*args, **kwargs)
                    now = datetime.now()
                    start = now.strftime('%d/%m/%Y %H:%M:%S')
                    print(f'Time:{start}  {func.__name__}  Result:{result}')
                except Exception as e:
                    now = datetime.now()
                    start = now.strftime('%d/%m/%Y %H:%M:%S')
                    print(f'Time:{start}  {func.__name__}  Error:{e}  Input: {args}')
                    raise ValueError(e)
        return inner
    return wrapper
