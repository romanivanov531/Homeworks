import unittest

import pandas as pd
import pytest
from unittest.mock import patch, mock_open

from src.transactions_reader import transactions_read_excel, transactions_read_csv


def test_transactions_reader_csv_wrong_direction():
    with pytest.raises(Exception) as e:
        transactions_read_csv('wrong_direction')
        assert e == 'FileNotFoundError: [Errno 2] No such file or directory: "direction"'


class TestTransactionsReadCsv(unittest.TestCase):

    def test_transactions_read_csv(self):
        mock_data = """header1,header2
value1,value2
value3,value4
"""
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = transactions_read_csv('dummy.csv')
            expected = [
                {'header1': 'value1', 'header2': 'value2'},
                {'header1': 'value3', 'header2': 'value4'}
            ]
            self.assertEqual(result, expected)

    def test_transactions_read_csv_with_error(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = transactions_read_csv('dummy.csv')
            self.assertEqual(result, [])


class TestTransactionsReadExcel(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_transactions_read_excel(self, mock_read_excel):
        mock_df = pd.DataFrame({"header1": ["value1", "value3"], "header2": ["value2", "value4"]})
        mock_read_excel.return_value = mock_df

        result = transactions_read_excel('dummy.xlsx')

        expected = [
            {'header1': 'value1', 'header2': 'value2'},
            {'header1': 'value3', 'header2': 'value4'}
        ]

        self.assertEqual(result, expected)

    @patch('pandas.read_excel')
    def test_transactions_read_excel_with_error(self, mock_read_excel):
        mock_read_excel.side_effect = Exception('Ошибка чтения')

        result = transactions_read_excel('dummy.xlsx')

        self.assertEqual(result, [])
