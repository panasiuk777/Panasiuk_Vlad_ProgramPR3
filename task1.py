name = "Vlad"
surname = "Panasiuk"
group = "IT31"
year = 2009


def print_card():
    """Print student's card using personal data."""
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def print_card_args(name, surname, group="IT31", year=2009):
    """Print student's card using function arguments."""
    print(f"{name} {surname}, {group}, {year}")


print(f"{name} {surname}, {group}")

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()

print("--- positional arguments ---")
print_card_args("Vlad", "Panasiuk", "IT31", 2009)

print("--- keyword arguments ---")
print_card_args(year=2009, group="IT31", surname="Panasiuk", name="Vlad")

print("--- mixed arguments ---")
print_card_args("Vlad", "Panasiuk", group="IT31", year=2009)

print("--- default group ---")
print_card_args("Vlad", "Panasiuk", year=2009)

print("--- missing arguments ---")
try:
    print_card_args("Vlad")
except TypeError as error:
    print(error)

print("--- invalid syntax ---")
print('The call print_card_args(name="Vlad", "Panasiuk") causes a SyntaxError before the program runs.')