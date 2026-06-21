from src.processing import filter_by_state, search_by_keyword, sort_by_date
from src.transactions_reader import transactions_read_csv, transactions_read_excel
from src.utils import take_operations_info
from src.widget import get_date, mask_account_card


def main():

    # file_type = input('Привет! Добро пожаловать в программу работы'
    #                    'с банковскими транзакциями.'
    #                    'Выберете необходимый пункт меню:\n'
    #                    '1. Получить информацию о транзакциях из JSON-файла\n'
    #                    '2. Получить информацию о транзакциях из CSV-файла\n'
    #                    '3. Получить информацию о транзакциях из XLSX-файла\n')
    #
    # status_code = input('Введите статус, по которому необходимо выполнить фильтрацию. '
    #                     'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    global transaction_list
    while True:
        file_type = input(
            "Привет! Добро пожаловать в программу работы"
            "с банковскими транзакциями."
            "Выберете необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        if file_type in ["1", "2", "3"]:
            break
        else:
            print("Выберете значение от 1 до 3\n")

    while True:
        status_code = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if status_code.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")

    date_sort = input("Отсортировать операции по дате? Да/Нет\n")

    date_up = input("Отсортировать по возрастанию или по убыванию?\n")

    value_code = input("Выводить только рублевые транзакции? Да/Нет\n")

    key_word_choose = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if key_word_choose.lower() == "да":
        key_word = input()
    else:
        key_word = None

    if file_type == "1":
        transaction_list = take_operations_info("data/operations.json")
    elif file_type == "2":
        transaction_list = transactions_read_csv("data/transactions.csv")
    elif file_type == "3":
        transaction_list = transactions_read_excel("data/transactions_excel.xlsx")

    transaction_filter_by_state = filter_by_state(transaction_list, status_code.upper())
    if date_sort.lower() == "да":
        if date_up.lower() == "по возрастанию":
            transaction_filter_by_date = sort_by_date(transaction_filter_by_state)
        else:
            transaction_filter_by_date = sort_by_date(transaction_filter_by_state, False)
    else:
        transaction_filter_by_date = transaction_filter_by_state
    print(transaction_filter_by_date)
    if value_code.lower() == "да":
        transaction_filter_by_value_code = [
            operation
            for operation in transaction_filter_by_date
            if operation.get("operationAmount").get("currency").get("code") == "RUB"
        ]

    else:
        transaction_filter_by_value_code = transaction_filter_by_date
    print(transaction_filter_by_value_code)
    if key_word:
        transaction_filtered_by_key_word = search_by_keyword(transaction_filter_by_value_code, key_word)
    else:
        transaction_filtered_by_key_word = transaction_filter_by_value_code

    print("Распечатываю итоговый список транзакций...")
    print(f'Всего банковских операций в выборке: {len(transaction_filtered_by_key_word)}')
    for operation in transaction_filtered_by_key_word:
        print(
            f"{get_date(operation.get('date'))} {operation.get('description')}\n"
            f"{mask_account_card(str(operation.get('from')))} -> {mask_account_card(str(operation.get('to')))}\n"
            f"Сумма:{operation.get('operationAmount').get('amount')} "
            f"{operation.get('operationAmount').get('currency').get('code')}"
        )


if __name__ == "__main__":
    main()
