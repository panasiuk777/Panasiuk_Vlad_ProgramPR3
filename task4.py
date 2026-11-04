
import csv
import math
import random
import sys
import time
from pathlib import Path
from datetime import datetime

NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"

# Заміни на свій справжній рік народження
BIRTH_YEAR = 2007

random.seed(BIRTH_YEAR)

print(f"{NAME} {SURNAME}, {GROUP}")

history_file = Path(__file__).parent / "history.csv"

score = 0
start_time = time.time()

for number in range(1, 6):
    question_type = random.choice(
        ["sqrt", "factorial", "gcd", "comb", "percent"]
    )

    if question_type == "sqrt":
        n = random.randint(10, 100)
        question = f"√{n} (ціла частина кореня)"
        correct = math.isqrt(n)

    elif question_type == "factorial":
        n = random.randint(3, 7)
        question = f"{n}!"
        correct = math.factorial(n)

    elif question_type == "gcd":
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        question = f"НСД({a}, {b})"
        correct = math.gcd(a, b)

    elif question_type == "comb":
        n = random.randint(5, 10)
        k = random.randint(2, 4)
        question = f"C({n}, {k})"
        correct = math.comb(n, k)

    else:
        percent = random.randint(10, 90)
        n = random.randint(100, 500)
        question = f"{percent}% від {n}"
        correct = n * percent / 100

    print(f"\nПитання {number}/5: {question}")

    try:
        answer = float(input("Твоя відповідь: "))
    except ValueError:
        print("Некоректне введення. Відповідь не зараховано.")
        continue

    if math.isclose(answer, correct, rel_tol=1e-9):
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно. Правильна відповідь: {correct}")

duration = time.time() - start_time

print(f"\nРезультат: {score}/5")
print(f"Час виконання: {duration:.2f} секунд")

# Запис результату в історію
file_exists = history_file.exists()

try:
    with history_file.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        if not file_exists:
            writer.writerow(["Дата", "Ім'я", "Група", "Бали", "Час"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"{NAME} {SURNAME}",
            GROUP,
            score,
            f"{duration:.2f}"
        ])

except OSError as error:
    print(f"Помилка запису: {error}", file=sys.stderr)
    sys.exit(1)

# Пошук найкращого результату
best_score = score

try:
    with history_file.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            best_score = max(best_score, int(row["Бали"]))

except (OSError, ValueError, KeyError) as error:
    print(f"Помилка читання: {error}", file=sys.stderr)
    sys.exit(1)

print(f"Найкращий результат: {best_score}/5")
print(f"Історія збережена у: {history_file}")
