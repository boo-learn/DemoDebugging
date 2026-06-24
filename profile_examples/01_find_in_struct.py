import time

# Подготовка данных
BIG_AMOUNT = 100_000
search_elements = list(range(BIG_AMOUNT))
search_set = set(search_elements)

# Элементы, которые мы будем искать (половины нет в структуре)
items_to_find = list(range(BIG_AMOUNT - 5000, BIG_AMOUNT + 5000))

# Функция 1: Поиск в списке
def find_in_list():
    count = 0
    for item in items_to_find:
        if item in search_elements:
            count += 1
    return count

# Функция 2: Поиск в множестве
def find_in_set():
    count = 0
    for item in items_to_find:
        if item in search_set:
            count += 1
    return count