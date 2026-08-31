print("Vlad Panasiuk, IT31")

name = input("Enter your full name (Latin letters): ").strip()
age = int(input("Enter your age (integer): "))

if not name:
    print("Name was not entered")
    display_name = "Anonymous"
else:
    display_name = name

if age < 0:
    category = "invalid"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"{display_name}, your category is {category}")