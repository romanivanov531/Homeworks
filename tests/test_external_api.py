from unittest.mock import patch

from src.external_api import operation_amount


@patch('requests.request')
def test_operation_amount(mock_get, operation_info):
    mock_get.return_value.json.return_value = {"result": 1.0}
    assert operation_amount(operation_info) == 1.0
