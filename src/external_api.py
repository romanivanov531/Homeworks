import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def operation_amount(operation: dict) -> float | Exception:
    '''Функция для поиска суммы транзакций.
    Если валюта отличается от РУБ, проводит конвертацию с помощью внешнего API.
    Возвращает сумму транзакции.'''
    currency = operation.get('operationAmount')['currency']['code']
    amount = operation['operationAmount']['amount']
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {
        "apikey": f"{API_KEY}"
    }
    if currency != 'RUB':
        try:
            response = requests.request("GET", url, headers=headers)
            convert = response.json()
            return float(convert['result'])
        except Exception as e:
            return e
    else:
        return float(amount)
