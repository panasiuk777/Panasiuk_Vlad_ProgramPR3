import json
from datetime import date

print("Vlad Panasiuk, IT31")

# Створюємо словник з датою
data = {
    "owner": "Vlad Panasiuk",
    "date": date.today(),
    "amount": 250
}

# Спроба серіалізації без додаткових параметрів
try:
    json.dumps(data)
except TypeError as error:
    print("TypeError:", error)

# Спосіб 1: використання параметра default
def date_converter(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Unsupported type")

json_text = json.dumps(data, default=date_converter, ensure_ascii=False)
print("Method 1:", json_text)

# Спосіб 2: власні функції для перетворення
def prepare_data(obj):
    result = obj.copy()
    if isinstance(result.get("date"), date):
        result["date"] = result["date"].isoformat()
    return result

def restore_data(obj):
    result = obj.copy()
    if "date" in result:
        result["date"] = date.fromisoformat(result["date"])
    return result

# Записуємо JSON у файл
prepared = prepare_data(data)

with open("date_data.json", "w", encoding="utf-8") as file:
    json.dump(prepared, file, indent=2, ensure_ascii=False)

# Читаємо JSON і відновлюємо дату
with open("date_data.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

restored = restore_data(loaded)

print("Method 2: date restored")
print("Data matches:", restored == data)
print("Date type:", type(restored["date"]))