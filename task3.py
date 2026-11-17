
import requests
import sys

print("Vlad Panasiuk, IT31")

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.75,
    "longitude": 25.34,
    "current": "temperature_2m,wind_speed_10m"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]
    units = data["current_units"]

    print("City: Lutsk")
    print(
        f'Temperature: {current["temperature_2m"]} '
        f'{units["temperature_2m"]}'
    )
    print(
        f'Wind speed: {current["wind_speed_10m"]} '
        f'{units["wind_speed_10m"]}'
    )

except requests.RequestException as error:
    print(f"Network error: {error}", file=sys.stderr)
    sys.exit(1)
