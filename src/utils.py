import json
import os


def take_operations_info(directory: str) -> list:
    try:
        with open(f'/home/roman/PycharmProjects/Homeworks/data/{directory}', 'r') as file:
            operations_info = json.load(file)
        return list(operations_info)
    except Exception:
        return []
