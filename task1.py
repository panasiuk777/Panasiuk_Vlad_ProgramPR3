
import csv
import json
import os

print("Vlad Panasiuk, IT31")

input_file = "data/expenses.csv"
output_file = "data/expenses.json"

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    expenses = []

    for row in reader:
        expenses.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["comment"]
        })

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

size = os.path.getsize(output_file)

print(f"records: {len(expenses)}")
print(f"saved: {output_file} ({size} bytes)")
