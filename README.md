# Channel report pipeline

Собирает ежемесячный PPTX-отчёт по Telegram-каналу из JSON: метрики, графики, топ постов.

Стек: Python, pandas, matplotlib, python-pptx.

Данные только учебные (`data/samples/`), без выгрузок клиентов.

Автор: Юлия Богданова

## Запуск

Нужен Python 3.10+. В папке репозитория:

```powershell
pip install -r requirements.txt
python src/metrics.py
python src/charts.py
python src/report.py
```

Готовый файл: `output/report.pptx`.

Папка `output/` в git не попадает: презентация собирается у себя на компьютере из учебного JSON `data/samples/channel_month.json`.
