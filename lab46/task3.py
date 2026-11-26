
# Практична робота 21
# Завдання 3. Змінна класу та лічильник об'єктів
# Vlad Panasiuk, IT31
# Дата народження: 27.02.2009

class Expense:
    currency = "UAH"
    object_count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment
        Expense.object_count += 1

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def show(self):
        return f"{self.category}: {self.amount:.2f} {self.currency}"


expense1 = Expense("2026-11-01", "food", 120.50, "lunch")
expense2 = Expense("2026-11-02", "transport", 35.00, "bus")
expense3 = Expense("2026-11-03", "education", 450.00, "books")

print("Кількість створених об'єктів:", Expense.object_count)

print("\nВитрати у гривнях:")
for expense in [expense1, expense2, expense3]:
    print(expense.show())

Expense.set_currency("USD")

print("\nПісля зміни валюти:")
for expense in [expense1, expense2, expense3]:
    print(expense.show())

print("\nПоточна валюта класу:", Expense.currency)
