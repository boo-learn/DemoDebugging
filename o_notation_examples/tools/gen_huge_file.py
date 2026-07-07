import random
from datetime import datetime, timedelta

# Настройки генерации
FILE_NAME = "huge_production_log.txt"
NUM_LINES = 1_000_000  # 1 миллион строк выдаст файл примерно на 100-120 МБ

# Шаблоны для логов
SERVICES = ["auth-service", "payment-api", "user-profile", "gateway", "inventory-db"]
LEVELS = ["INFO", "INFO", "INFO", "WARNING", "ERROR", "INFO"]  # INFO чаще остальных
MESSAGES = {
    "INFO": [
        "User logged in successfully.",
        "Request processed in 45ms.",
        "Connection established to master database.",
        "Cache refreshed for key: user_session.",
        "API health check passed."
    ],
    "WARNING": [
        "Database pool utilization is high (82%).",
        "Slow query detected: SELECT * FROM orders WHERE...",
        "API rate limit reached for IP 192.168.1.45.",
        "Deprecated API endpoint called: /v1/users/old_list."
    ],
    "ERROR": [
        "Failed to process payment: Gateway Timeout.",
        "Database connection lost. Reconnecting...",
        "Permission denied for user_id=4039.",
        "Unexpected NullPointerException in serialization.",
        "Critical disk space warning: 92% used."
    ]
}


def generate_logs(file_path: str, lines_count: int) -> None:
    print(f"Начинаю генерацию {lines_count} строк в файл '{file_path}'...")

    start_time = datetime.now() - timedelta(days=1)  # Логи за последние сутки
    current_time = start_time
    time_increment = timedelta(seconds=24 * 3600 / lines_count)  # Равномерный шаг времени

    # Используем контекстный менеджер для безопасной работы с файлом
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(lines_count):
            # Шаг 1: Симулируем ход времени
            current_time += time_increment
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]

            # Шаг 2: Случайный выбор параметров
            service = random.choice(SERVICES)
            level = random.choice(LEVELS)
            message = random.choice(MESSAGES[level])

            # Шаг 3: Собираем строку лога
            log_line = f"{timestamp} | {level:<7} | {service:<12} | {message}\n"

            # Шаг 4: Пишем в файл
            file.write(log_line)

            # Раз в 10% прогресса выводим статус в консоль
            if (i + 1) % (lines_count // 10) == 0:
                print(f"Готово: {(i + 1) / lines_count * 100:.0f}%")

    print(f"Успешно завершено! Файл '{file_path}' готов к использованию.")


if __name__ == "__main__":
    generate_logs(FILE_NAME, NUM_LINES)