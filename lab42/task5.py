# Практична робота 19
# Завдання 5. Деструктор
# Vlad Panasiuk, IT31

class Wallet:
    def __init__(self, owner):
        self.owner = owner
        print(f"Гаманець власника {self.owner} створено")

    def __del__(self):
        print(f"Гаманець власника {self.owner} видалено")


print("Створення гаманця:")
wallet = Wallet("Влад Панасюк")

print("Створення другого посилання:")
other = wallet

print("Видалення першого посилання:")
del wallet

print("Об'єкт ще існує через друге посилання:")
print(other.owner)

print("Видалення останнього посилання:")
del other

print("Кінець програми")