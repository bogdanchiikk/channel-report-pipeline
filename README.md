# Channel report pipeline

Собирает ежемесячный PPTX-отчёт по Telegram-каналу из JSON: метрики, графики, топ постов.

Стек: Python, pandas, matplotlib, python-pptx.

Данные только учебные (`data/samples/`), без выгрузок клиентов.

Автор: Юлия Богданова

## Что в презентации

Файл `output/report.pptx` содержит пять слайдов: титул, KPI (старт, финиш, пришло, ушло, чистый прирост), график подписчиков, график joined vs left, топ-5 постов по просмотрам.

Папка `output/` в git не попадает. Пути к JSON и к выходной папке задаются в `config.example.json`.

## Запуск

Нужен Python 3.10+. Из корня репозитория:

```bash
pip install -r requirements.txt
python -m src.metrics
python -m src.charts
python -m src.report
pytest
```
