schedule = {
    "Mon": ["Programming", "Ukrainian", "Computer science"],
    "Tue": ["Programming", "IT Pravo", "Database in information systems"],
    "Wed": ["Foreign language", "Database in information systems", "Development of web resource"],
    "Thu": ["Programming", "Development of web resource", "Computer science"],
    "Fri": ["Foreign language", "Development of web resource", "IT Pravo"]
}

print("Weekly schedule:")
print("-" * 75)
print(f"{'Day':<8}{'Number of classes':<20}Subjects")
print("-" * 75)

for day, subjects in schedule.items():
    print(f"{day:<8}{len(subjects):<20}{', '.join(subjects)}")

print("-" * 75)

total_classes = sum(len(subjects) for subjects in schedule.values())
print(f"\nTotal classes per week: {total_classes}")

busiest_day = max(schedule, key=lambda day: len(schedule[day]))
print(f"Busiest day: {busiest_day} ({len(schedule[busiest_day])} classes)")

all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print(f"\nDifferent subjects: {all_subjects}")
print(f"Number of different subjects: {len(all_subjects)}")

monday_subjects = set(schedule["Mon"])
wednesday_subjects = set(schedule["Wed"])

common_subjects = monday_subjects & wednesday_subjects

print(f"\nSubjects on Monday and Wednesday: {common_subjects}")

monday_only = monday_subjects - wednesday_subjects

print(f"Subjects on Monday but not on Wednesday: {monday_only}")


def count_subjects(schedule):
    subject_counts = {}

    for subjects in schedule.values():
        for subject in subjects:
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return subject_counts


subject_counts = count_subjects(schedule)

print("\nSubject counts:")
for subject, count in subject_counts.items():
    print(f"{subject}: {count}")


rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nSubject rating:")

for position, (subject, count) in enumerate(rating, start=1):
    print(f"{position}. {subject} - {count} classes")
