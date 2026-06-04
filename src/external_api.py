import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY_EXCHANGE_RATES")


def operation_amount(operation: dict) -> float:
    currency = operation['operationAmount']['currency']['code']
    amount = operation['operationAmount']['amount']

    if currency != 'RUB':
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {
            "apikey": f"{API_KEY}"
        }
        response = requests.request("GET", url, headers=headers)
        convert = response.json()

        return float(convert['result'])
    else:
        return float(amount)
