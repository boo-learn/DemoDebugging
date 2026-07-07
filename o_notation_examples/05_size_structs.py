import sys
from pympler import asizeof

data_list = [x for x in range(10_000_000)]
data_tuple = tuple([x for x in range(10_000_000)])
data_set = {x for x in range(10_000_000)}

print(f"Список занимает: {sys.getsizeof(data_list) / (1024 * 1024):.2f} МБ")
print(f"Полный размер списка: {asizeof.asizeof(data_list) / (1024 * 1024):.2f} МБ")
print(f"Кортеж занимает: {sys.getsizeof(data_tuple) / (1024 * 1024):.2f} МБ")
print(f"Полный размер кортежа: {asizeof.asizeof(data_tuple) / (1024 * 1024):.2f} МБ")
print(f"set занимает: {sys.getsizeof(data_set) / (1024 * 1024):.2f} МБ")
print(f"Полный размер set: {asizeof.asizeof(data_set) / (1024 * 1024):.2f} МБ")