
# Практична робота 18
# Завдання 2. Атрибути класу та екземпляра
# Vlad Panasiuk, IT31

class Student:
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return year - self.birth_year

    def card(self, year=2026):
        return (
            "+---------------------+\n"
            f"| {self.full_name():<19} |\n"
            f"| group: {self.group:<12} |\n"
            f"| age in {year}: {self.age(year):<9} |\n"
            "+---------------------+"
        )


# Створення об'єктів
student1 = Student("Vlad", "Panasiuk", "IT31", 2008)
student2 = Student("Andrii", "Shevchenko", "IT31", 2007)

# Атрибут класу
print("College через клас:", Student.college)
print("College через об'єкт:", student1.college)

# Зміна атрибута одного об'єкта
student1.college = "My College"

print("\nПісля зміни:")
print("Student 1:", student1.college)
print("Student 2:", student2.college)

# Кількість студентів
print("\nКількість студентів:", Student.count)

# Словники атрибутів
print("\nАтрибути student1:")
print(student1.__dict__)

print("\nАтрибути student2:")
print(student2.__dict__)

print("\nАтрибути класу:")
print(Student.__dict__)
