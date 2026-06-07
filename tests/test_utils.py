import json
from unittest.mock import Mock

from src.utils import take_operations_info


def test_take_operation_info():
    mock_result = Mock(return_value=[{'name': 'value'}])
    json.load = mock_result
    assert take_operations_info("/home/roman/PycharmProjects/Homeworks/data/operations.json") == [{'name': 'value'}]


def test_take_operation_info_wrong_directory():
    result = take_operations_info("ddd")
    assert result == []
