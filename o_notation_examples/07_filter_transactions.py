from datetime import datetime
from typing import TypedDict
from tools.decorators import benchmark


class Transaction(TypedDict):
    amount: int
    date: str


# 1. Плохой подход
@benchmark()
def filter_transactions_bad(transactions: list[Transaction]) -> list[Transaction]:
    valid_transactions = []
    for tx in transactions:
        # Инвариант внутри цикла — datetime.strptime("2026-01-01", ...) вызывается 500 000 раз
        if datetime.strptime(tx["date"], "%Y-%m-%d") > datetime.strptime(
            "2026-01-01", "%Y-%m-%d"
        ):
            valid_transactions.append(tx)
    return valid_transactions


# 2. Оптимизированный (хороший) подход
@benchmark()
def filter_transactions_good(transactions: list[Transaction]) -> list[Transaction]:
    valid_transactions = []
    # Выносим инвариант — парсим граничную дату ОДИН раз до начала цикла
    deadline_date = datetime.strptime("2026-01-01", "%Y-%m-%d")

    for tx in transactions:
        if datetime.strptime(tx["date"], "%Y-%m-%d") > deadline_date:
            valid_transactions.append(tx)
    return valid_transactions


if __name__ == "__main__":
    print("Генерация тестовых данных...")
    test_transactions: list[Transaction] = [
        {"amount": 100, "date": "2026-07-07"} for _ in range(500_000)
    ]

    print("\nЗапуск неоптимизированной функции...")
    res_bad = filter_transactions_bad(test_transactions)

    print("\nЗапуск оптимизированной функции...")
    res_good = filter_transactions_good(test_transactions)