name = "Vlad"
surname = "Panasiuk"
group = "IT31"


def create_subjects():
    return [
        ("Programming", 3, 77),
        ("English", 2, 88),
        ("Database", 2, 99),
        ("IT Law", 2, 89)
    ]


def print_table(subjects):
    print(f"{name} {surname}, {group}")
    print(f"{'#':<4}{'Subject':<20}{'Pairs':>7}{'Grade':>8}")

    for number, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{number:<4}{title:<20}{pairs:>7}{grade:>8}")


def total_pairs(subjects):
    return sum(subject[1] for subject in subjects)


def find_most_pairs(subjects):
    return max(subjects, key=lambda subject: subject[1])


def find_lowest_grade(subjects):
    return min(subjects, key=lambda subject: subject[2])


def get_titles(subjects):
    return [subject[0] for subject in subjects]


def get_grades(subjects):
    return [subject[2] for subject in subjects]


def get_average(grades):
    return sum(grades) / len(grades)


def get_high_grades(subjects):
    return [title for title, pairs, grade in subjects if grade >= 10]


def print_histogram(subjects):
    for title, pairs, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_lowest(subjects):
    lowest = find_lowest_grade(subjects)
    lowest_title = lowest[0]
    old_grade = lowest[2]

    new_grade = min(old_grade + 2, 12)

    updated_subjects = []

    for title, pairs, grade in subjects:
        if title == lowest_title:
            updated_subjects.append((title, pairs, new_grade))
        else:
            updated_subjects.append((title, pairs, grade))

    print(f"Retake: {lowest_title} {old_grade} -> {new_grade}")

    return updated_subjects


def main():
    subjects = create_subjects()

    # 2. Таблиця предметів
    print_table(subjects)

    # 3. Загальна кількість пар
    print("\nPairs per week:", total_pairs(subjects))

    # 4. Предмет з найбільшою кількістю пар
    most_pairs = find_most_pairs(subjects)
    print(f"Most pairs: {most_pairs[0]} ({most_pairs[1]})")

    # Предмет із найнижчою оцінкою
    lowest = find_lowest_grade(subjects)
    print(f"Weakest subject: {lowest[0]} ({lowest[2]})")

    # 5. Назви, оцінки та середня оцінка
    titles = get_titles(subjects)
    grades = get_grades(subjects)
    average = get_average(grades)

    print("Titles:", titles)
    print(f"Grades: {grades}, average: {average:.2f}")

    # 6. Предмети з оцінкою 10 і вище
    print("Grade 10+:", get_high_grades(subjects))

    # 7. Гістограма
    print("\nHistogram:")
    print_histogram(subjects)

    # 8. Перездача предмета з найнижчою оцінкою
    subjects = retake_lowest(subjects)

    print("Subjects:", subjects)


if __name__ == "__main__":
    main()