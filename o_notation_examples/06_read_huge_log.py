def read_huge_file(file_path):
    """Построчное чтение файла без загрузки его целиком в RAM"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Функция отдает строку и засыпает до следующего вызова
            yield line.strip()

# Создается объект-генератор, файл еще даже не читался
log_generator = read_huge_file("huge_production_log.txt")

# Данные читаются из диска по одной строке строго в момент итерации
for log_line in log_generator:
    if "ERROR" in log_line:
        print(log_line) # Обработали строку и забыли, память свободна!