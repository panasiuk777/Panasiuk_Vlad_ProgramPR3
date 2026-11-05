
import pytest

from expenses import parse_line, load_expenses, total_by_category


# Завдання 2. Перевірка правильного рядка

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_date():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["date"] == "2026-09-21"


def test_parse_line_comment():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["comment"] == "lunch"


# Завдання 3. Перевірка винятків

def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


# Завдання 4. Параметризований тест

@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-11-01;food;120.50;lunch", "food", 120.50),
        ("2026-11-02;transport;35.00;bus", "transport", 35.00),
        ("2026-11-03;food;85.00;groceries", "food", 85.00),
        ("2026-09-21;food;85.50;lunch", "food", 85.50),
        ("2026-09-22;food;14.50;coffee", "food", 14.50),
    ],
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount


# Завдання 5. Тимчасовий файл

def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )

    totals = total_by_category(load_expenses(path))

    assert totals == {"food": 100.0}


# Перевірка справжнього файлу витрат

def test_real_expenses():
    records = load_expenses("data/expenses.csv")

    totals = total_by_category(records)

    assert totals == {
        "food": 205.50,
        "transport": 35.00,
    }
