
# Практична робота 20
# Завдання 3. Види витрат
# Vlad Panasiuk, IT31

class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


expenses = [
    RecurringExpense("2026-11-01", "Транспорт", 35.00, 20),
    RecurringExpense("2026-11-02", "Мобільний зв'язок", 200.00, 1),
    SharedExpense("2026-11-03", "Оренда", 12000.00, 3),
    SharedExpense("2026-11-04", "Інтернет", 600.00, 2)
]

total = 0

print("Місячні витрати:")

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(
        expense.date,
        expense.category,
        "-",
        round(cost, 2),
        "грн"
    )

print("Загальна місячна вартість:", round(total, 2), "грн")
