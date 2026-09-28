# 1. Оцінки одним рядком
grades_string = "77, 88, 99, 89, 100"

# 2. Отримуємо список цілих чисел
grades = [int(grade) for grade in grades_string.split(", ")]

# Назви предметів
subjects_string = "Programming, English, Database, IT Law, Web-Development"

# Отримуємо список предметів
subjects = subjects_string.split(", ")

# 3. Середня, найвища та найнижча оцінки
average = sum(grades) / len(grades)

print("Grades:", grades)
print(f"Average grade: {average:.2f}")
print("Highest grade:", max(grades))
print("Lowest grade:", min(grades))

# 4. Оцінки через |
grades_joined = " | ".join(str(grade) for grade in grades)

print("\nGrades joined:")
print(grades_joined)

# 5-6. Таблиця предметів та оцінок
print("\nTable:")
print(f"{'No.':<5}{'Subject':<20}{'Grade':>5}")
print("-" * 30)

for number, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{number:<5}{subject:<20}{grade:>5}")

# 7. Предмет із найдовшою назвою
longest_subject = max(subjects, key=len)

print("\nLongest subject:", longest_subject)
print("Number of characters:", len(longest_subject))
