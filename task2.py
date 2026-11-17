import json
from datetime import date

print("Vlad Panasiuk, IT31")

input_file = "data/expenses.json"
output_file = "data/expenses_updated.json"

# Читаємо JSON
with open(input_file, "r", encoding="utf-8") as file:
    expenses = json.load(file)

# Додаємо новий запис
new_expense = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 100.0,
    "comment": "Новий запис"
}

expenses.append(new_expense)
added = 1

# Видаляємо записи із сумою менше 10
old_count = len(expenses)
expenses = [item for item in expenses if item["amount"] >= 10]
deleted = old_count - len(expenses)

# Записуємо результат у новий файл
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print