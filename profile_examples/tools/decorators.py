import functools
import time
from typing import Any, Callable


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор, который измеряет и выводит время выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()

        # Выполняем саму функцию
        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(
            f" [Таймер] Функция '{func.__name__}' выполнилась за {execution_time:.6f} сек."
        )
        return result

    return wrapper

def benchmark(runs: int = 1):
    """Декоратор для замера среднего времени выполнения функции.

    :param runs: Количество запусков функции для усреднения результата.
    """
    if runs < 1:
        raise ValueError("Количество запусков должно быть не менее 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0.0
            result = None  # Типизируем возвращаемое значение

            for _ in range(runs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                total_time += end_time - start_time

            avg_time = total_time / runs
            print(
                f"[{func.__name__}] Запусков: {runs}. "
                f"Среднее время выполнения: {avg_time:.6f} сек."
            )
            return result

        return wrapper

    return decorator