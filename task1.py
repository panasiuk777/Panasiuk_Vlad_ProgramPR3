me = {
    "name": "Vlad",
    "surname": "Panasiuk",
    "group": "IT-31",
    "city": "Lutsk",
    "birth_year": 2009,
    "hobbies": ["car", "sport", "motorbike"]
}

print("Information about me:")
for key, value in me.items():
    print(f"{key}: {value}")

print("\nKeys:")
print(list(me.keys()))
print(f"Number of pairs: {len(me)}")

print(f"\nGroup: {me['group']}")

print(f"Email: {me.get('email', 'unknown')}")

me["email"] = "tpanasiuk12@gmail.com"

me["city"] = "Kyiv"

removed_birth_year = me.pop("birth_year")
print(f"Removed birth year: {removed_birth_year}")

print("\nDictionary after changes:")
print(me)

print(f"\nDoes the dictionary contain 'phone'? {'phone' in me}")
