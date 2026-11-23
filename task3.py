
# Практична робота 18
# Завдання 3. Клас Expense
# Vlad Panasiuk, IT31

import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        from datetime import datetime

        formatted_date = datetime.strptime(
            self.date, "%Y-%m-%d"
        ).strftime("%d.%m.%Y")

        return (
            f"{formatted_date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )


# Читання CSV-файлу
file_path = Path(__file__).parent / "data" / "expenses.csv"

expenses = []

with open(file_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        expense = Expense(
            row["date"],
            row["category"],
            row["amount"],
            row["comment"]
        )
        expenses.append(expense)


# Виведення результатів
limit = 150

print("Усього витрат:", len(expenses))
print("Великі витрати (понад", limit, "грн):")

for expense in expenses:
    if expense.is_big(limit):
        print(expense.describe())
