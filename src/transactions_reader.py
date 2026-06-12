import csv

import pandas as pd


def transactions_read_csv(directory: str) -> list:
    try:
        with open(f'{directory}', 'r', encoding='utf-8') as file:
            df = csv.DictReader(file)
            return [row for row in df]
    except Exception as e:
        print(e)
        return []


def transactions_read_excel(directory: str) -> list:
    try:
        transactions_df = pd.read_excel(directory)
        transactions_list = transactions_df.to_dict(orient='records')
        return list(transactions_list)
    except Exception as e:
        print(e)
        return []
