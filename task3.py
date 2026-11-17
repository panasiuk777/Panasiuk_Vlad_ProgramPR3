import json
import sys
import os
import csv

print("Vlad Panasiuk, IT31")

settings_file = "settings.json"
expenses_file = "data/expenses.csv"

default_settings = {
    "owner": "Vlad Panasiuk",
    "group": "IT31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not os.path.exists(settings_file):
    with open(settings_file, "w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)

    print("settings.json not found, default created")
    sys.exit(0)

try:
    with open(settings_file, "r", encoding="utf-8") as file:
        settings = json.load(file)

except json.JSONDecodeError as error:
    print(f"JSON error in line {error.lineno}", file=sys.stderr)
    sys.exit(1)

total_spent = 0

with open(expenses_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_spent += float(row["amount"])

limit = float(settings["monthly_limit"])
left = limit - total_spent

print(f"limit: {limit:.2f} {settings['currency']}, spent: {total_spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")