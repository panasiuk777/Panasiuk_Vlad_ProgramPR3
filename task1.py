# 1. Навмисно недбало записане повне ім'я
full_name = "  pANASIUK   vLAD   yURIYOVYCH  "

# 2. Робимо рядок охайним за допомогою split(), join() і title()
words = full_name.split()
full_name = " ".join(words).title()

print("Full name:", full_name)
print("Length:", len(full_name))

# 3. Розпаковуємо ім'я на окремі частини
surname, name, patronymic = full_name.split()

# 4. Робота з прізвищем та ім'ям
print("\nFirst character of surname:", surname[0])
print("Last character of surname:", surname[-1])
print("Surname backwards:", surname[::-1])

print("Name format:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Initials:", surname[0] + name[0] + patronymic[0])

# Кількість голосних у повному імені
vowels = "aeiouy"
vowel_count = sum(1 for char in full_name.lower() if char in vowels)

print("Number of vowels:", vowel_count)

# 5. Робота з групою
group = "IT31"

dash_position = group.find("-")

# У групі IT31 немає дефіса, тому демонструємо роботу
# з частиною до та після дефіса через find() і зрізи.
if dash_position != -1:
    before_dash = group[:dash_position]
    after_dash = group[dash_position + 1:]
else:
    # Для IT31 логічно вважаємо IT частиною до номера
    before_dash = group[:2]
    after_dash = group[2:]

print("\nGroup:", group)
print("Part before dash:", before_dash)
print("Part after dash:", after_dash)
print("Is the part after dash a number:", after_dash.isdigit())

# 6. Логін та електронна пошта
login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"

print("\nLogin:", login)
print("Email:", email)
