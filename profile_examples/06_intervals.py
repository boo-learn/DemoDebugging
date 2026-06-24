import time

# Генерируем тестовые интервалы времени
# Формат: (start_time, end_time)
INTERVALS = [(i, i + 5) for i in range(5_000)]
# Добавим несколько явно пересекающихся интервалов для теста
INTERVALS.append((5, 12))
INTERVALS.append((10, 15))


@profile
def find_overlapping_intervals_naive(intervals: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """[CPU Bound] Поиск пересечений через вложенные циклы — O(N^2).

    Множества (set) тут не помогут, так как мы сравниваем интервалы «каждый с каждым».
    """
    overlaps = []
    n = len(intervals)

    for i in range(n):
        for j in range(i + 1, n):
            start1, end1 = intervals[i]
            start2, end2 = intervals[j]

            # Условие пересечения двух интервалов
            if start1 < end2 and start2 < end1:
                overlaps.append((intervals[i], intervals[j]))

    return overlaps


def main():
    print("Поиск пересечений (наивный алгоритм)...")
    start = time.perf_counter()

    result = find_overlapping_intervals_naive(INTERVALS)

    end = time.perf_counter()
    print(f"Найдено пересечений: {len(result)}")
    print(f"Время выполнения: {end - start:.2f} сек.")


if __name__ == "__main__":
    main()