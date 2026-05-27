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
    start = now.strftime('%d/%m/%y %H:%M:%S')
    assert captured.out == f'Start:{start}  my_function  result:3\n'


def test_log_error_empty_dec():
    with pytest.raises(ValueError):
        @log('')
        def error_func(a, b):
            return a + b
        error_func('', 2)
