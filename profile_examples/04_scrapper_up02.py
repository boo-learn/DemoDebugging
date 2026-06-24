import asyncio
import time
import aiohttp

ITEMS_TO_FETCH = list(range(1, 51))


async def fetch_data_from_api(session: aiohttp.ClientSession, item_id: int) -> dict:
    """[Оптимизировано: асинхронный I/O Bound]"""
    url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"

    async with session.get(url) as response:
        return await response.json()


def find_duplicates_naive(data_list: list[dict]) -> list[dict]:
    """[CPU Bound] Квадратичный алгоритм O(N^2) для поиска дубликатов."""
    unique_items = []

    for item in data_list:
        if item["title"] not in [u["title"] for u in unique_items]:
            unique_items.append(item)

    return unique_items


# Главная функция тоже становится асинхронной
async def main():
    print("Запуск асинхронного скрейпера...")
    start_time = time.perf_counter()

    # 1. Создаем асинхронную сессию
    async with aiohttp.ClientSession() as session:
        # Создаем список "задач" (tasks) для каждого ID
        tasks = [fetch_data_from_api(session, item_id) for item_id in ITEMS_TO_FETCH]

        # Запускаем все задачи конкурентно и ждем их общего завершения
        all_data = await asyncio.gather(*tasks)

    # Увеличиваем массив для проверки CPU
    large_dataset = all_data * 1000

    # 2. Обрабатываем данные
    print(f"Обработка {len(large_dataset)} элементов...")
    clean_data = find_duplicates_naive(large_dataset)

    end_time = time.perf_counter()
    print(f"Готово! Уникальных элементов: {len(clean_data)}")
    print(f"Общее время работы: {end_time - start_time:.2f} сек.")


if __name__ == "__main__":
    # Запуск асинхронного event loop (актуально для Python 3.7+)
    asyncio.run(main())