name = "Vlad"
surname = "Panasiuk"
group = "IT31"
y = 2009


def print_age(year):
    """Print the age and return nothing."""
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    """Return age for the given year."""
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age

    print("after return")


print(f"{name} {surname}, {group}")

print("--- print_age ---")
print_age(y)

print("--- print_age inside print ---")
print(print_age(y))

age = get_age(y)
print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

print(f"Age in 2030: {get_age(y, current_year=2030)}")

print("--- invalid year ---")
print(f"Invalid year 3000 gives: {get_age(3000)}")

print("--- print_age multiplied ---")
try:
    print_age(y) * 12
except TypeError as error:
    print(error)