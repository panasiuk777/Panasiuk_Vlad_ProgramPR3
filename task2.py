
import csv
import math
import sys
from pathlib import Path
from datetime import date, datetime, timedelta

NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"

print(f"{NAME} {SURNAME}, {GROUP}")

# Перевірка наявності файлу
if not DATA_FILE.is_file():
    print(f"Помилка: файл не знайдено: {DATA_FILE}", file=sys.stderr)
    sys.exit(1)

expenses = []

# Читання витрат із CSV
try:
    with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        for line_number, row in enumerate(reader, start=1):
            if not row or not any(value.strip() for value in row):
                continue

            if row[0].strip().startswith("#"):
                continue

            try:
                if len(row) < 3:
                    raise ValueError("недостатньо стовпців")

                expense_date = date.fromisoformat(row[0].strip())
                category = row[1].strip()
                amount = float(row[2].strip())

                if not math.isfinite(amount) or amount < 0:
                    raise ValueError("некоректна сума")

                expenses.append((expense_date, category, amount))

            except ValueError as error:
                print(
                    f"Попередження: рядок {line_number} пропущено: {error}",
                    file=sys.stderr
                )

except OSError as error:
    print(f"Помилка читання файлу: {error}", file=sys.stderr)
    sys.exit(1)

if not expenses:
    print("Немає коректних записів про витрати.")
    sys.exit(1)

# Загальна сума витрат
total = math.fsum(item[2] for item in expenses)

dates = [item[0] for item in expenses]
first_date = min(dates)
last_date = max(dates)

# Формування щоденних сум
daily = {}
current = first_date

while current <= last_date:
    daily[current] = 0.0
    current += timedelta(days=1)

for expense_date, category, amount in expenses:
    daily[expense_date] += amount

daily_values = list(daily.values())

# Середня сума та стандартне відхилення
average = math.fsum(daily_values) / len(daily_values)

variance = math.fsum(
    (value - average) ** 2 for value in daily_values
) / len(daily_values)

std_deviation = math.sqrt(variance)

# Витрати за днями тижня
weekday_names = [
    "Понеділок", "Вівторок", "Середа",
    "Четвер", "П'ятниця", "Субота", "Неділя"
]

weekday_totals = [0.0] * 7

for expense_date, category, amount in expenses:
    weekday_totals[expense_date.weekday()] += amount

# День із найбільшими витратами
top_day = max(daily, key=daily.get)

# Дні без витрат
zero_days = [day for day, amount in daily.items() if amount == 0]

# Визначення кількості днів у місяці
def days_in_month(year, month):
    first_day = date(year, month, 1)

    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)

    return (next_month - first_day).days

month_length = days_in_month(last_date.year, last_date.month)
days_passed = last_date.day
days_remaining = month_length - days_passed

# Прогноз витрат за місяць
month_total = math.fsum(
    amount for expense_date, category, amount in expenses
    if expense_date.year == last_date.year
    and expense_date.month == last_date.month
)

monthly_average = month_total / days_passed
forecast = monthly_average * month_length

# Виведення результатів
print("\n--- Загальна інформація ---")
print(f"Кількість записів: {len(expenses)}")
print(f"Період: {first_date} — {last_date}")
print(f"Загальні витрати: {total:.2f} грн")
print(f"Середні витрати за день: {average:.2f} грн")
print(f"Стандартне відхилення: {std_deviation:.2f} грн")

print("\n--- Витрати за днями тижня ---")
for index, name in enumerate(weekday_names):
    print(f"{name}: {weekday_totals[index]:.2f} грн")

print("\n--- Найбільші та нульові витрати ---")
print(f"День із найбільшими витратами: {top_day}")
print(f"Сума: {daily[top_day]:.2f} грн")
print(f"Днів без витрат: {len(zero_days)}")

for day in zero_days:
    print(f"  {day}")

print("\n--- Прогноз за місяць ---")
print(f"Днів у місяці: {month_length}")
print(f"Днів минуло: {days_passed}")
print(f"Днів залишилося: {days_remaining}")
print(f"Сума за місяць на цей момент: {month_total:.2f} грн")
print(f"Прогноз витрат за місяць: {forecast:.2f} грн")

# Перевірка кількості днів у заданих місяцях
print("\n--- Перевірка календаря ---")
print(f"Грудень 2026: {days_in_month(2026, 12)} днів")
print(f"Лютий 2028: {days_in_month(2028, 2)} днів")
