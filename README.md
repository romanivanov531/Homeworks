# Виджет банковских операций
## Описание
Виджет предоставляет пользователям возможность удобно и быстро отслеживать свои транзакции.
## Структура проекта
  1. src/masks.py - модуль, для хранения функций по маскировке счетов и карт
  2. src/widget.py - модуль, осуществляющий маскировку счетов или карт
  3. src/processing.py - модуль для сортировки операций
  4. scr/decorators.py - модуль для хранения декораторов
  5. src/utils.py - модуль для чтения файлов json 
  6. src/external_api.py - модуль для конвертации валюты операций
  7. src/transactions_reader.py
  8. tests/test_....py - модули для тестирования 
  9. data/operations.json
  10. main.py - исполнительный модуль 
## Установка
  1. Скопируйте репозиторий
     ```
     git clone https://github.com/romanivanov531/SkyPro_Chapter_2.git
     ```
  2. Установите poetry
     ```
     poetry install
     ```
  3. Установите зависимости
     Например:
     ```
     poetry add <addiction>
     ```
     Все зависимости перечислены в файле pyproject.toml
## Пример использования
Убедитесь, что установили все необходимые зависимости.
Можно запустить файл ```widget.py```, например:
  ```
  python3 src/widget.py Visa Platinum 7000792289606361
  ```
## Тестирование Pytest
  1. Установите Pytest и плагин pytest-cov
     ```
     poetry add --group dev pytest
     poetry add --group dev pytest-cov
     ```
     Или
     ```
     pip install pytest
     pip install pytest-cov
     ```
  2. Запустите Pytest
     * Для отдельных модулей
     ```
     pytest tests/test_module.py
     ```
     * Общая проверка всех модулей
     ```
     pytest
     ```
  3. Проверьте покрытие тестами и сохраните результат
     ```
     pytest --cov
     ```
     ```
     pytest --cov=src --cov-report=html
     ```
     * Отчет покрытия тестами в директории tests_log/index.html

## Использование программы
  1. Запустите main.py
  2. Следуйте инструкциям на экране
     