
# Практична робота 20
# Завдання 2. isinstance, issubclass та MRO
# Vlad Panasiuk, IT31

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def describe(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name, surname, group):
        super().__init__(name, surname)
        self.group = group

    def describe(self):
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name, surname, group, phone):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self):
        return f"{super().describe()}, group leader, {self.phone}"


person = Person("Ivan", "Petrenko")
student = Student("Vlad", "Panasiuk", "IT31")
leader = GroupLeader("Olena", "Koval", "IT31", "+380 67 000 00 00")

print("ТАБЛИЦЯ isinstance:")

objects = [
    ("person", person),
    ("student", student),
    ("leader", leader)
]

classes = [Person, Student, GroupLeader]

for object_name, obj in objects:
    for cls in classes:
        print(f"isinstance({object_name}, {cls.__name__}) = {isinstance(obj, cls)}")

print("\nТАБЛИЦЯ issubclass:")

for child in classes:
    for parent in classes:
        print(
            f"issubclass({child.__name__}, {parent.__name__}) = "
            f"{issubclass(child, parent)}"
        )

print("\nПорядок пошуку методів (__mro__):")
print(GroupLeader.__mro__)

print("\nОпис старости:")
print(leader.describe())
