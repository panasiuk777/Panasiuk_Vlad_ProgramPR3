
import requests
import json
import os
import sys
from datetime import datetime, timezone

print("Vlad Panasiuk, IT31")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"

os.makedirs("cache", exist_ok=True)

try:
    rates = None

    # Перевіряємо, чи існує кеш
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache = json.load(file)

        fetched_at = datetime.fromisoformat(cache["fetched_at"])
        age = (datetime.now(timezone.utc) - fetched_at).total_seconds()

        if 0 <= age < 3600:
            rates = cache["rates"]
            print(f"source: cache (age {int(age)} s)")

    # Якщо кеш відсутній або застарілий — запитуємо API
    if rates is None:
        response = requests.get(
            URL,
            params={"json": ""},
            timeout=10
        )
        response.raise_for_status()

        rates = response.json()

        cache = {
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "rates": rates
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(cache, file, ensure_ascii=False, indent=4)

        print("source: api (cache saved)")

    print("currencies:", len(rates))

    for currency in rates:
        if currency["cc"] in ["USD", "EUR"]:
            print(
                f'{currency["cc"]}: {currency["rate"]:.2f} UAH'
            )

except (requests.RequestException, OSError, ValueError, KeyError, TypeError) as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
