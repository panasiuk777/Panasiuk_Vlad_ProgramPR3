
import requests
import sys

print("Vlad Panasiuk, IT31")

def test_connection():
    try:
        requests.get(
            "https://api.open-meteo.com/v1/forecast",
            timeout=10
        )
    except requests.ConnectionError:
        print("ConnectionError: немає з'єднання з інтернетом")
        return
    print("Connection is available")


def test_http_error():
    try:
        response = requests.get(
            "https://api.open-meteo.com/invalid_path",
            timeout=10
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("HTTPError: сервер повернув помилку HTTP")


def test_timeout():
    try:
        requests.get(
            "https://api.open-meteo.com/v1/forecast",
            timeout=0.001
        )
    except requests.Timeout:
        print("Timeout: час очікування запиту вичерпано")


test_connection()
test_http_error()
test_timeout()
