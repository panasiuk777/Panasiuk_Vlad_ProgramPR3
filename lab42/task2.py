
# Практична робота 19
# Завдання 2. Інкапсуляція
# Vlad Panasiuk, IT31

class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance -= amount

    def show_balance(self):
        return self.__balance


wallet = Wallet("Влад Панасюк", 2500.50)

print("Власник:", wallet.owner)
print("Початковий баланс:", wallet.show_balance())

wallet.deposit(500)
print("Після поповнення:", wallet.show_balance())

wallet.withdraw(300)
print("Після зняття:", wallet.show_balance())

try:
    wallet.withdraw(5000)
except ValueError as error:
    print("Помилка:", error)

# Спроба прямого доступу до приватного атрибута
try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка доступу:", error)

# Доступ через перетворене ім'я
print("Доступ через name mangling:", wallet._Wallet__balance)
