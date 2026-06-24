import time
import requests

# Список ID для проверки (имитируем парсинг 50 страниц)
ITEMS_TO_FETCH = list(range(1, 51))


def fetch_data_from_api(session: requests.Session, item_id: int) -> dict:
    """[Оптимизировано: I/O Bound] Использование существующего TCP-соединения сессии."""
    url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"
    # Делаем запрос через сессию, а не через модуль requests
    response = session.get(url)
    return response.json()


def find_duplicates_naive(data_list: list[dict]) -> list[dict]:
    """[CPU Bound] Квадратичный алгоритм O(N^2) для поиска дубликатов."""
    unique_items = []

    for item in data_list:
        if item["title"] not in [u["title"] for u in unique_items]:
            unique_items.append(item)

    return unique_items


def main():
    print("Запуск скрейпера...")
    start_time = time.perf_counter()

    # 1. Собираем данные
    all_data = []
    with requests.Session() as session:
        for item_id in ITEMS_TO_FETCH:
            data = fetch_data_from_api(session, item_id)
            all_data.append(data)

    # Искусственно увеличим массив данных
    large_dataset = all_data * 1000

    # 2. Обрабатываем данные (Тормозит тут: CPU Bound)
    print(f"Обработка {len(large_dataset)} элементов...")
    clean_data = find_duplicates_naive(large_dataset)

    end_time = time.perf_counter()
    print(f"Готово! Уникальных элементов: {len(clean_data)}")
    print(f"Общее время работы: {end_time - start_time:.2f} сек.")


if __name__ == "__main__":
    main()