import time

# Генерируем тестовые интервалы времени
# Формат: (start_time, end_time)
INTERVALS = [(i, i + 5) for i in range(5_000)]
# Добавим несколько явно пересекающихся интервалов для теста
INTERVALS.append((5, 12))
INTERVALS.append((10, 15))



@profile
def find_overlapping_intervals_optimized(intervals: list[tuple[int, int]]) -> list[
    tuple[tuple[int, int], tuple[int, int]]]:
    """[Оптимизировано: CPU Bound] Сортировка + один проход — O(N log N)."""
    overlaps = []

    # 1. Сортируем интервалы по времени начала (в Python встроенный Timsort очень быстрый)
    # Сложность: O(N log N)
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # 2. Проверяем только соседние элементы за один проход — O(N)
    for i in range(len(sorted_intervals) - 1):
        current_start, current_end = sorted_intervals[i]
        next_start, next_end = sorted_intervals[i + 1]

        # Так как список отсортирован, проверяем только пересечение со следующим
        if next_start < current_end:
            overlaps.append((sorted_intervals[i], sorted_intervals[i + 1]))

    return overlaps


def main():
    print("Поиск пересечений (оптимизированный алгоритм)...")
    start = time.perf_counter()

    result = find_overlapping_intervals_optimized(INTERVALS)

    end = time.perf_counter()
    print(f"Найдено пересечений: {len(result)}")
    print(f"Время выполнения: {end - start:.4f} сек.")


if __name__ == "__main__":
    main()