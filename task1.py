name = "Vlad"
surname = "Panasiuk"
group = "IT31"

# c = кількість літер у прізвищі Panasiuk
c = len(surname)

grades = [77, 88, 99, 89, 100, 96, 87, 79]

print(f"{name} {surname}, {group}")
print("Grades:", grades)

# 2. Основна інформація про оцінки
print("Number of grades:", len(grades))
print("Sum:", sum(grades))
print("Best grade:", max(grades))
print("Worst grade:", min(grades))
print(f"Average: {sum(grades) / len(grades):.2f}")

# 3. Оцінки від найкращої до найгіршої
sorted_grades = sorted(grades, reverse=True)

print("\nSorted grades:", sorted_grades)
print("Original grades:", grades)

# 4. Три найкращі та три найгірші
print("Three best grades:", sorted_grades[:3])
print("Three worst grades:", sorted_grades[-3:])

# 5. Позиція найгіршої оцінки
worst_grade = min(grades)
worst_position = grades.index(worst_grade) + 1

print("Position of the worst grade:", worst_position)

# 6. Оцінки, вищі за середнє
average = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average]

print("Grades above average:", above_average)
print("Number above average:", len(above_average))

# 7. Перевірка наявності 12 і 1
print("Is there a 12?", 12 in grades)
print("Is there a 1?", 1 in grades)

# 8. Зміни списку

# Додаємо оцінку c % 12 + 1
new_grade = c % 12 + 1
grades.append(new_grade)
print("\nAfter append:", grades)

# Вставляємо 12 на початок
grades.insert(0, 12)
print("After insert:", grades)

# Вилучаємо найгіршу оцінку
grades.remove(min(grades))
print("After removing worst grade:", grades)

# Вилучаємо останню оцінку
removed_grade = grades.pop()
print("Removed last grade:", removed_grade)
print("After pop:", grades)

# 9. Скільки разів трапляється 12
print("Number of 12s:", grades.count(12))

# 10. Сортуємо сам список grades
sort_result = grades.sort()

print("\nResult of grades.sort():", sort_result)
print("Sorted grades:", grades)