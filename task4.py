
# Практична робота 18
# Завдання 4. Клас ExpenseBook
# Vlad Panasiuk, IT31

import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def describe(self):
        return (
            f"{self.date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.category == category
        )

    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]


# Читання CSV
file_path = Path(__file__).parent / "data" / "expenses.csv"

book = ExpenseBook()

with open(file_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        expense = Expense(
            row["date"],
            row["category"],
            row["amount"],
            row["comment"]
        )
        book.add(expense)


# Аналіз витрат
print("Загальна сума витрат:", f"{book.total():.2f} грн")

print("\nВитрати за категоріями:")

categories = sorted(set(e.category for e in book.expenses))

for category in categories:
    print(f"{category}: {book.by_category(category):.2f} грн")

print("\nТри найбільші витрати:")

for expense in book.top(3):
    print(expense.describe())
