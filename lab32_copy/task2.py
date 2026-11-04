
import csv
import sys
from pathlib import Path
from collections import defaultdict
from math import fsum
from tabulate import tabulate

NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"

print(f"{NAME} {SURNAME}, {GROUP}")

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"

if not DATA_FILE.is_file():
    print("Помилка: файл expenses.csv не знайдено", file=sys.stderr)
    sys.exit(1)

categories = defaultdict(list)

try:
    with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row or not any(value.strip() for value in row):
                continue

            if row[0].strip().startswith("#"):
                continue

            try:
                if len(row) < 3:
                    raise ValueError("недостатньо стовпців")

                category = row[1].strip()
                amount = float(row[2].strip())

                if not category or amount < 0:
                    raise ValueError("некоректні дані")

                categories[category].append(amount)

            except ValueError as error:
                print(f"Попередження: {row} — {error}", file=sys.stderr)

except OSError as error:
    print(f"Помилка читання файлу: {error}", file=sys.stderr)
    sys.exit(1)

if not categories:
    print("Немає коректних витрат.")
    sys.exit(1)

rows = []
all_amounts = []

for category, amounts in sorted(categories.items()):
    total = fsum(amounts)
    rows.append([category, len(amounts), f"{total:.2f}"])
    all_amounts.extend(amounts)

rows.append(["TOTAL", len(all_amounts), f"{fsum(all_amounts):.2f}"])

print(tabulate(
    rows,
    headers=["category", "count", "total"],
    tablefmt="github"
))
