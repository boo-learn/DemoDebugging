## Команды запуска

Запуск встроенного профайлера
```bash
python -m cProfile script.py
```

Запуск встроенного профайлера с визуализацией
```bash
python -m cProfile -o program_stats.prof script.py
```
```bash
snakeviz program_stats.prof
```

Запуск профайлера pyinstrument
```bash
pyinstrument script.py
```

Запуск профайлера pyinstrument с визуализацией
```bash
pyinstrument -o index.html script.py
```