import pytest
from src.utils import take_operations_info


def test_take_operation_info():
    result = take_operations_info('operations.json')
    assert result == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
        ]

def test_take_operation_info_wrong_directory():
    result = take_operations_info('ddd')
    assert result == []

