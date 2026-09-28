surname = "Panasiuk"

# 1. Список літер у нижньому регістрі
letters = list(surname.lower())
c = len(surname)

print("Surname:", surname)
print("Letters:", letters)
print("Length c:", c)

# 2. Перша, середня та остання літера
print("\nFirst letter:", letters[0])
print("Middle letter:", letters[len(letters) // 2])

# Останню літеру отримуємо двома способами
print("Last letter ([-1]):", letters[-1])
print("Last letter (index):", letters[len(letters) - 1])

# 3. Робота зі зрізами
print("\nFirst three letters:", letters[:3])
print("Except first three:", letters[3:])
print("Every second letter:", letters[::2])
print("Reverse order:", letters[::-1])
print("Last two letters:", letters[-2:])

# Позиція c дорівнює 8, тому після неї елементів немає
print("Part of length 5 starting from position c:", letters[c:c + 5])

# 4. Унікальні літери у порядку першої появи
unique = []

for letter in letters:
    if letter not in unique:
        unique.append(letter)

print("\nUnique letters:", unique)

# Пошук повторів
repeated = False

for letter in unique:
    count = letters.count(letter)

    if count > 1:
        print(f"Letter '{letter}' appears {count} times")
        repeated = True

if not repeated:
    print("No repeated letters")

# 5. Літери в алфавітному порядку
print("Alphabetical order:", sorted(letters))
