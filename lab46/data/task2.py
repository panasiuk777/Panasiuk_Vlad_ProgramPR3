
# Практична робота 21
# Завдання 2. Статичні методи
# Vlad Panasiuk, IT31
# Дата народження: 27.02.2009

from datetime import datetime


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")

        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        return cls(date, category, float(amount), comment)


print("Перевірка дат:")
print("2026-11-26:", Expense.is_valid_date("2026-11-26"))
print("2026-02-30:", Expense.is_valid_date("2026-02-30"))

print("\nПеревірка сум:")
print("120.50:", Expense.is_valid_amount("120.50"))
print("-50:", Expense.is_valid_amount("-50"))
print("abc:", Expense.is_valid_amount("abc"))

print("\nПеревірка CSV-рядків:")

lines = [
    "2026-11-01;food;120.50;lunch",
    "2026-02-30;transport;35.00;bus",
    "2026-11-03;food;-85.00;groceries",
    "2026-11-04;education;450.00;books"
]

for line in lines:
    try:
        expense = Expense.from_csv_line(line)
        print("Успішно:", expense.category, expense.amount)
    except ValueError as error:
        print("Пропущено:", error, "|", line)
