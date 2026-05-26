import pytest
from black import datetime

from src.decorators import log


def test_log(capsys):
    @log('')
    def my_function(a, b):
        return a + b
    my_function(1, 2)
    captured = capsys.readouterr()
    now = datetime.now()
    start = now.strftime('%d/%m/%Y %H:%M:%S')
    assert captured.out == f'Time:{start}  my_function  Result:3\n'


def test_log_error_in_func_args(capsys):
    @log(filename='log.txt')
    def error_function(a, b):
        return a + b
    with pytest.raises(ValueError):
        error_function('', 3)
        captured = capsys.readouterr()
        assert captured.out == 'can only concatenate str (not "int") to str'
