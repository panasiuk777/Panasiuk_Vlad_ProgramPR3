from pathlib import Path
from datetime import datetime
import sys


NAME = "Vladik"
SURNAME = "Panasiuk"
GROUP = "IT31"
BIRTH_DAY = 27

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
EXPENSES_FILE = DATA_DIR / "expenses.csv"


def usage():
    print("usage: python3 task3.py add <date> <category> <amount> <note>")
    print("       python3 task3.py list")
    print("       python3 task3.py report")


def validate_record(date, category, amount_text, note):
    try:
        amount = float(amount_text)
    except ValueError:
        return None, f"bad amount '{amount_text}'"

    if amount <= 0:
        return None, f"amount must be positive, got {amount:.2f}"

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None, f"bad date '{date}'"

    if not category or not note:
        return None, "empty category or note"

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }, None


def read_expenses():
    if not EXPENSES_FILE.exists():
        raise FileNotFoundError

    if EXPENSES_FILE.is_dir():
        raise IsADirectoryError

    expenses = []
    bad_lines = []

    with EXPENSES_FILE.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";")

            if len(parts) != 4:
                bad_lines.append(
                    (number, f"expected 4 fields, got {len(parts)}")
                )
                continue

            date, category, amount, note = parts

            record, error = validate_record(
                date, category, amount, note
            )

            if error:
                bad_lines.append((number, error))
                continue

            expenses.append(record)

    return expenses, bad_lines


def handle_file_error():
    try:
        read_expenses()
    except FileNotFoundError:
        print(
            "error: data/expenses.csv not found",
            file=sys.stderr
        )
        return 1
    except IsADirectoryError:
        print(
            "error: data/expenses.csv is a directory, not a file",
            file=sys.stderr
        )
        return 1
    except UnicodeDecodeError:
        print(
            "error: data/expenses.csv is not a UTF-8 text file",
            file=sys.stderr
        )
        return 1

    return 0


def add_expense(args):
    if len(args) < 4:
        usage()
        return 2

    date = args[0]
    category = args[1]
    amount = args[2]
    note = " ".join(args[3:])

    record, error = validate_record(
        date, category, amount, note
    )

    if error:
        print(f"error: {error}", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1

    DATA_DIR.mkdir(exist_ok=True)

    if not EXPENSES_FILE.exists():
        EXPENSES_FILE.write_text(
            "# date;category;amount;note\n",
            encoding="utf-8"
        )

    with EXPENSES_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"{record['date']};"
            f"{record['category']};"
            f"{record['amount']:.2f};"
            f"{record['note']}\n"
        )

    print(
        f"added: {record['date']} "
        f"{record['category']} "
        f"{record['amount']:.2f} "
        f"({record['note']})"
    )

    return 0


def list_expenses():
    try:
        expenses, bad_lines = read_expenses()
    except FileNotFoundError:
        print(
            "error: data/expenses.csv not found",
            file=sys.stderr
        )
        return 1
    except IsADirectoryError:
        print(
            "error: data/expenses.csv is a directory, not a file",
            file=sys.stderr
        )
        return 1
    except UnicodeDecodeError:
        print(
            "error: data/expenses.csv is not a UTF-8 text file",
            file=sys.stderr
        )
        return 1

    if expenses:
        print("date        category       amount  note")

        for item in expenses:
            print(
                f"{item['date']}  "
                f"{item['category']:<13} "
                f"{item['amount']:>8.2f}  "
                f"{item['note']}"
            )

        total = sum(item["amount"] for item in expenses)

        print()
        print(
            f"{len(expenses)} records, total {total:.2f}"
        )
    else:
        print("no valid expenses")

    if bad_lines:
        print(
            f"skipped {len(bad_lines)} bad line(s):",
            file=sys.stderr
        )

        for number, reason in bad_lines:
            print(
                f"  line {number}: {reason}",
                file=sys.stderr
            )

    return 0


def make_report():
    try:
        expenses, bad_lines = read_expenses()
    except FileNotFoundError:
        print(
            "error: data/expenses.csv not found",
            file=sys.stderr
        )
        return 1
    except IsADirectoryError:
        print(
            "error: data/expenses.csv is a directory, not a file",
            file=sys.stderr
        )
        return 1
    except UnicodeDecodeError:
        print(
            "error: data/expenses.csv is not a UTF-8 text file",
            file=sys.stderr
        )
        return 1

    if not expenses:
        print(
            "error: nothing to report, no valid records",
            file=sys.stderr
        )
        return 1

    total = sum(item["amount"] for item in expenses)

    dates = [item["date"] for item in expenses]

    categories = {}

    for item in expenses:
        category = item["category"]

        if category not in categories:
            categories[category] = {
                "count": 0,
                "total": 0
            }

        categories[category]["count"] += 1
        categories[category]["total"] += item["amount"]

    sorted_categories = sorted(
        categories.items(),
        key=lambda x: x[1]["total"],
        reverse=True
    )

    lines = []

    lines.append(
        f"Expenses report for {NAME} {SURNAME} ({GROUP})"
    )
    lines.append(
        f"Period: {min(dates)} .. {max(dates)}"
    )
    lines.append(f"Records: {len(expenses)}")
    lines.append("")

    lines.append(
        f"{'category':<15}"
        f"{'count':>7}"
        f"{'total':>11}"
        f"{'share':>8}  chart"
    )

    lines.append("-" * 55)

    for category, data in sorted_categories:
        share = data["total"] / total * 100
        chart = "#" * int(share / 5)

        lines.append(
            f"{category:<15}"
            f"{data['count']:>7}"
            f"{data['total']:>11.2f}"
            f"{share:>7.1f}%  "
            f"{chart}"
        )

    lines.append("-" * 55)

    lines.append(
        f"{'total':<15}"
        f"{len(expenses):>7}"
        f"{total:>11.2f}"
        f"{100:>7.1f}%"
    )

    daily = {}

    for item in expenses:
        daily[item["date"]] = (
            daily.get(item["date"], 0)
            + item["amount"]
        )

    top_day = max(
        daily.items(),
        key=lambda x: x[1]
    )

    most_expensive = max(
        expenses,
        key=lambda x: x["amount"]
    )

    average = total / len(daily)

    lines.append("")
    lines.append(
        f"Top day: {top_day[0]} ({top_day[1]:.2f})"
    )
    lines.append(
        f"Most expensive: "
        f"{most_expensive['category']} "
        f"{most_expensive['amount']:.2f} "
        f"({most_expensive['note']})"
    )
    lines.append(
        f"Average per day: {average:.2f}"
    )

    report = "\n".join(lines)

    REPORTS_DIR = SCRIPT_DIR / "reports"
    REPORTS_DIR.mkdir(exist_ok=True)

    report_file = REPORTS_DIR / "expenses_report.txt"

    report_file.write_text(
        report + "\n",
        encoding="utf-8"
    )

    print(report)
    print()
    print(f"report saved to: {report_file}")

    if bad_lines:
        print(
            f"skipped {len(bad_lines)} bad line(s):",
            file=sys.stderr
        )

        for number, reason in bad_lines:
            print(
                f"  line {number}: {reason}",
                file=sys.stderr
            )

    return 0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if len(sys.argv) < 2:
        usage()
        return 2

    command = sys.argv[1]

    if command == "add":
        return add_expense(sys.argv[2:])

    if command == "list":
        return list_expenses()

    if command == "report":
        return make_report()

    print(
        f"error: unknown command {command}",
        file=sys.stderr
    )
    usage()
    return 2


if __name__ == "__main__":
    sys.exit(main())
