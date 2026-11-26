
# Практична робота 20
# Завдання 1. Наслідування класів
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


student = Student("Vlad", "Panasiuk", "IT31")
leader = GroupLeader("Olena", "Koval", "IT31", "+380 67 000 00 00")

print(student.describe())
print(leader.describe())
