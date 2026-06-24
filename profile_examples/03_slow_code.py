import math
import time

def heavy_math():
    # Огромное количество вызовов встроенной функции
    return [math.sqrt(x) for x in range(1_000_000)]


def network_wait():
    # Имитация ожидания ответа сети
    time.sleep(1)


def main():
    heavy_math()
    network_wait()


if __name__ == "__main__":
    main()