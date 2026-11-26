# Практична робота 19
# Завдання 4. Робота з CSV
# Vlad Panasiuk, IT31

import csv

class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.owner = owner
        self.balance = round(balance, 2)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance = round(self.balance - amount, 2)

wallet = Wallet("Влад Панасюк", 777777)

print("Початковий бюджет:", wallet.balance, "грн")

with open("data/expenses.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for expense in reader:
        amount = float(expense["amount"])

        try:
            wallet.withdraw(amount)
            print(
                expense["date"],
                expense["category"],
                amount,
                "грн — залишок:",
                wallet.balance,
                "грн"
            )
        except ValueError as error:
            print("Витрату зупинено:", error)
            break

print("Залишок бюджету:", wallet.balance, "грн")