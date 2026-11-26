
# Практична робота 21
# Завдання 4. Поліморфізм
# Vlad Panasiuk, IT31
# Дата народження: 27.02.2009

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def balance_change(self):
        return 0


operations = [
    Income("Стипендія / підробіток", 2600.00),
    Expense("food", 120.50),
    Expense("transport", 35.00),
    Expense("food", 85.00),
    Expense("education", 450.00),
    Expense("entertainment", 200.00),
    Expense("transport", 50.00),
    Expense("food", 320.00),
    Transfer("Переказ між власними картками", 500.00)
]

income_total = 0
expenses_total = 0
transfers_total = 0
balance = 0

for operation in operations:
    change = operation.balance_change()
    balance += change

    if change > 0:
        income_total += change
    elif change < 0:
        expenses_total += change
    else:
        transfers_total += change

print("Vlad Panasiuk, IT31")
print(f"income:    {income_total:10.2f}")
print(f"expenses:  {expenses_total:10.2f}")
print(f"transfers: {transfers_total:10.2f}")
print(f"balance:   {balance:10.2f}")
