import time

# Имитируем какую-то работу
def heavy_calculation():
    return sum(i * i for i in range(10_000_000))

# Точка отсчета
start_time = time.perf_counter()

heavy_calculation()

# Конечная точка
end_time = time.perf_counter()

duration = end_time - start_time
print(f"Функция выполнялась: {duration:.4f} секунд")