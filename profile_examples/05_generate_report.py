import time

# Имитируем 50 000 записей логов
LOG_RECORDS = [f"User_{i%1000} accessed page_{i}" for i in range(50_000)]

# @profile
def generate_report_naive(records: list[str]) -> str:
    """[CPU Bound] Очень медленная генерация отчета."""
    report = ""
    unique_users = []

    for record in records:
        # Ошибка 1: Квадратичное копирование строк в памяти при каждом знаке +
        report += record + "\n"

        # Ошибка 2: Линейный поиск по списку unique_users (тоже O(N))
        user = record.split()[0]
        if user not in unique_users:
            unique_users.append(user)

    # Допишем в конец отчета количество уникальных
    report += f"Total unique users: {len(unique_users)}"
    return report


def main():
    print("Генерация отчета (старый метод)...")
    start = time.perf_counter()

    result = generate_report_naive(LOG_RECORDS)

    end = time.perf_counter()
    print(f"Размер отчета: {len(result)} символов.")
    print(f"Время выполнения: {end - start:.2f} сек.")


if __name__ == "__main__":
    main()