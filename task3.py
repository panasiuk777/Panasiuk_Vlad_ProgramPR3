
from pathlib import Path
from datetime import datetime
from math import log
import argparse
import shutil
import sys

NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"

parser = argparse.ArgumentParser(
    usage="python task3.py [--dry-run] <dir>"
)
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("directory", type=Path)
args = parser.parse_args()

print(f"{NAME} {SURNAME}, {GROUP}")

directory = args.directory

if not directory.is_dir():
    print(f"error: {directory} is not a directory", file=sys.stderr)
    sys.exit(1)

files = [p for p in directory.iterdir() if p.is_file()]

if not files:
    print("No files found.")
    sys.exit(0)

def format_size(size):
    units = ["B", "KB", "MB", "GB"]

    if size == 0:
        return "0.0 B"

    index = min(int(log(size, 1024)), 3)
    value = size / (1024 ** index)

    return f"{value:.1f} {units[index]}"

# Сортування за датою зміни
files.sort(key=lambda p: p.stat().st_mtime)

# Формування плану переміщення
plan = []

for file in files:
    stat = file.stat()
    modified = datetime.fromtimestamp(stat.st_mtime)
    folder_name = modified.strftime("%Y-%m")
    destination = directory / folder_name / file.name

    plan.append((file, destination, stat.st_size, modified))

# Перевірка всіх конфліктів до переміщення
for source, destination, size, modified in plan:
    if destination.exists():
        print(
            f"error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

# Виведення плану
folders = set()

for source, destination, size, modified in plan:
    folders.add(destination.parent)
    print(
        f"{source.name:<20} {format_size(size):>8}  "
        f"{modified:%d.%m.%Y %H:%M}  -> "
        f"{destination.parent.name}/"
    )

if args.dry_run:
    print(
        f"{len(files)} files, {len(folders)} folders "
        "(dry run, nothing moved)"
    )
    sys.exit(0)


# Переміщення файлів
for source, destination, size, modified in plan:
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.rename(destination)

# Створення звіту
report_dir = Path(__file__).parent / "reports"
report_dir.mkdir(exist_ok=True)

now = datetime.now()
report_file = report_dir / f"organize_{now:%Y%m%d_%H%M}.txt"

with report_file.open("w", encoding="utf-8") as report:
    report.write(f"{NAME} {SURNAME}, {GROUP}\n")
    report.write(f"Date: {now:%d.%m.%Y %H:%M}\n")
    report.write(f"Moved files: {len(files)}\n\n")

    for source, destination, size, modified in plan:
        report.write(
            f"{source.name} -> {destination.parent.name}/\n"
        )

print(f"{len(files)} files, {len(folders)} folders")
print(f"report saved to: {report_file}")
