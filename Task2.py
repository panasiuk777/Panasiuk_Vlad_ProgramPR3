from pathlib import Path
from datetime import datetime


NAME = "Vladik"
SURNAME = "Panasiuk"

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
RUNS_FILE = DATA_DIR / "runs.log"


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def add_run(path, number):
    path.parent.mkdir(exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};{NAME} {SURNAME}\n")


def show_history(path, last=3):
    if not path.exists():
        print("runs so far: 0")
        return

    records = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(";")

            if len(parts) == 3:
                records.append(parts)

    print(f"runs so far: {len(records)}")
    print("last runs:")

    for number, stamp, name in records[-last:]:
        print(f"  #{number}  {stamp}  {name}")

    if records:
        print(f"first run was at {records[0][1]}")


def main():
    previous_runs = count_runs(RUNS_FILE)
    current_run = previous_runs + 1

    file_was_created = not RUNS_FILE.exists()

    add_run(RUNS_FILE, current_run)

    print(f"Hello, {NAME} {SURNAME}! This is run number {current_run}.")

    if file_was_created:
        print("runs.log was just created.")

    show_history(RUNS_FILE)


if __name__ == "__main__":
    main()
