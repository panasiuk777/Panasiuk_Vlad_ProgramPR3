
# Практична робота 19
# Завдання 1. Конструктор з перевіркою
# Vlad Panasiuk, IT31

class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        self.owner = owner
        self.balance = round(balance, 2)


# Створення коректного гаманця
wallet = Wallet("Влад Панасюк", 2500.50)

print("Власник:", wallet.owner)
print("Баланс:", wallet.balance, "грн")

# Спроба створити гаманець без імені
try:
    wallet2 = Wallet("", 1000)
except ValueError as error:
    print("Помилка:", error)

# Спроба створити гаманець з від'ємним балансом
try:
    wallet3 = Wallet("Влад Панасюк", -500)
except ValueError as error:
    print("Помилка:", error)
