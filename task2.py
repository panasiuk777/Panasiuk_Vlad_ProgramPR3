import requests
import csv
import sys

print("Vlad Panasiuk, IT31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
EXPENSES_FILE = "data/expenses.csv"

try:
    # Рахуємо загальні витрати
    total = 0

    with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["amount"])

    # Отримуємо курси USD та EUR окремими запитами
    rates = {}

    for code in ["USD", "EUR"]:
        response = requests.get(
            URL,
            params={"valcode": code, "json": ""},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        rates[code] = data[0]["rate"]
        rate_date = data[0]["exchangedate"]

    usd = total / rates["USD"]
    eur = total / rates["EUR"]

    print("rate date:", rate_date)
    print(f"total: {total:.2f} UAH = {usd:.2f} USD = {eur:.2f} EUR")

except (requests.RequestException, OSError, ValueError, KeyError, IndexError) as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)