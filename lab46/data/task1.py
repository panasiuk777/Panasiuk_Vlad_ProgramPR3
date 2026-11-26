
# Практична робота 21
# Завдання 1. Альтернативні конструктори
# Vlad Panasiuk, IT31
# Дата народження: 27.02.2009

import csv
import json

class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")
        return cls(date, category, amount, comment)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["date"],
            data["category"],
            data["amount"],
            data.get("comment", "")
        )

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ")
        category = input("Категорія: ")
        amount = float(input("Сума: "))
        comment = input("Коментар: ")
        return cls(date, category, amount, comment)


expense = Expense.from_csv_line("2026-09-21;food;85.50;lunch")
print("Створено з CSV-рядка:", expense.category, expense.amount)

with open("data/expenses.csv", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    csv_expenses = [
        Expense(
            row["date"],
            row["category"],
            row["amount"],
            row["comment"]
        )
        for row in csv_reader
    ]

with open("data/expenses.json", encoding="utf-8") as file:
    json_data = json.load(file)
    json_expenses = [Expense.from_dict(row) for row in json_data]

print("Кількість витрат у CSV:", len(csv_expenses))
print("Кількість витрат у JSON:", len(json_expenses))

print("\nПерша витрата з CSV:")
print(csv_expenses[0].date, csv_expenses[0].category,
      csv_expenses[0].amount, csv_expenses[0].comment)

print("\nПерша витрата з JSON:")
print(json_expenses[0].date, json_expenses[0].category,
      json_expenses[0].amount, json_expenses[0].comment)
