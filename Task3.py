from pathlib import Path
import sys


NAME = "Vladik"
SURNAME = "Panasiuk"
GROUP = "IT31"

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
REPORTS_DIR = SCRIPT_DIR / "reports"

EXPENSES_FILE = DATA_DIR / "expenses.csv"
REPORT_FILE = REPORTS_DIR / "expenses_report.txt"

HEADER = "# date;category;amount;note"


def usage():
    print("usage: python3 task3.py add <date> <category> <amount> <note>")
    print("       python3 task3.py list")
    print("       python3 task3.py report")


def ensure_file():
    DATA_DIR.mkdir(exist_ok=True)

    if not EXPENSES_FILE.exists():
        EXPENSES_FILE.write_text(HEADER + "\n", encoding="utf-8")


def read_expenses():
    if not EXPENSES_FILE.exists():
        return []

    expenses = []

    with EXPENSES_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";")

            if len(parts) != 4:
                continue

            date, category, amount, note = parts

            try:
                amount = float(amount)
            except ValueError:
                continue

            expenses.append({
                "date": date,
                "category": category,
                "amount": amount,
                "note": note
            })

    return expenses


def add_expense(args):
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        usage()
        return

    date = args[0]
    category = args[1]
    amount_text = args[2]
    note = " ".join(args[3:])

    try:
        amount = float(amount_text)
    except ValueError:
        print("error: amount must be a number")
        return

    ensure_file()

    with EXPENSES_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"{date};{category};{amount:.2f};{note}\n"
        )

    print(
        f"added: {date} {category} "
        f"{amount:.2f} ({note})"
    )


def list_expenses():
    expenses = read_expenses()

    if not expenses:
        print("no expenses")
        return

    date_width = max(
        len("date"),
        max(len(item["date"]) for item in expenses)
    )

    category_width = max(
        len("category"),
        max(len(item["category"]) for item in expenses)
    )

    amount_width = max(
        len("amount"),
        max(len(f"{item['amount']:.2f}") for item in expenses)
    )

    print(
        f"{'date':<{date_width}}  "
        f"{'category':<{category_width}}  "
        f"{'amount':>{amount_width}}  "
        f"note"
    )

    for item in expenses:
        print(
            f"{item['date']:<{date_width}}  "
            f"{item['category']:<{category_width}}  "
            f"{item['amount']:>{amount_width}.2f}  "
            f"{item['note']}"
        )

    total = sum(item["amount"] for item in expenses)

    print()
    print(f"{len(expenses)} records, total {total:.2f}")


def make_report():
    expenses = read_expenses()

    if not expenses:
        print("no expenses")
        return

    total = sum(item["amount"] for item in expenses)

    dates = [item["date"] for item in expenses]
    first_date = min(dates)
    last_date = max(dates)

    categories = {}

    for item in expenses:
        category = item["category"]

        if category not in categories:
            categories[category] = {
                "count": 0,
                "total": 0.0
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
        f"Period: {first_date} .. {last_date}"
    )
    lines.append(f"Records: {len(expenses)}")
    lines.append("")

    lines.append(
        f"{'category':<12}"
        f"{'count':>7}"
        f"{'total':>11}"
        f"{'share':>8}  "
        f"chart"
    )

    lines.append("-" * 52)

    for category, data in sorted_categories:
        share = data["total"] / total * 100

        # Один # за кожні 5%
        chart = "#" * int(share / 5)

        lines.append(
            f"{category:<12}"
            f"{data['count']:>7}"
            f"{data['total']:>11.2f}"
            f"{share:>7.1f}%  "
            f"{chart}"
        )

    lines.append("-" * 52)

    lines.append(
        f"{'total':<12}"
        f"{len(expenses):>7}"
        f"{total:>11.2f}"
        f"{100:>7.1f}%"
    )

    lines.append("")

    daily_totals = {}

    for item in expenses:
        date = item["date"]
        daily_totals[date] = (
            daily_totals.get(date, 0) + item["amount"]
        )

    top_day = max(
        daily_totals.items(),
        key=lambda x: x[1]
    )

    most_expensive = max(
        expenses,
        key=lambda item: item["amount"]
    )

    number_of_days = len(daily_totals)
    average_per_day = total / number_of_days

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
        f"Average per day: {average_per_day:.2f}"
    )

    report = "\n".join(lines)

    REPORTS_DIR.mkdir(exist_ok=True)

    REPORT_FILE.write_text(
        report + "\n",
        encoding="utf-8"
    )

    print(report)
    print()
    print(f"report saved to: {REPORT_FILE}")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    command = sys.argv[1]

    if command == "add":
        add_expense(sys.argv[2:])

    elif command == "list":
        list_expenses()

    elif command == "report":
        make_report()

    else:
        print(f"error: unknown command {command}")
        usage()


if __name__ == "__main__":
    main()
