from datetime import date
from unittest.mock import patch

from utils import get_summary, user_details, view_by_category


def test_user_details_adds_transaction_with_description_and_date():
    transactions = []

    with patch("builtins.input", side_effect=["Food", "Lunch at work", "1500"]):
        result = user_details(transactions, "expense")

    assert len(result) == 1
    transaction = result[0]
    assert transaction["type"] == "expense"
    assert transaction["category"] == "Food"
    assert transaction["description"] == "Lunch at work"
    assert transaction["amount"] == 1500
    assert transaction["date"] == date.today().isoformat()


def test_get_summary_calculates_income_expenses_and_balance():
    transactions = [
        {"type": "income", "category": "Salary", "description": "Monthly pay", "amount": 2500.00, "date": "2024-01-15"},
        {"type": "expense", "category": "Food", "description": "Groceries", "amount": 750.00, "date": "2024-01-16"},
        {"type": "expense", "category": "Transport", "description": "Fuel", "amount": 250.00, "date": "2024-01-17"},
    ]

    summary = get_summary(transactions)

    assert "Total Income:    ₦ 2,500.00" in summary
    assert "Total Expenses:  ₦ 1,000.00" in summary
    assert "Net Balance:     ₦ 1,500.00" in summary


def test_view_by_category_groups_expenses_and_includes_percentages():
    transactions = [
        {"type": "income", "category": "Salary", "description": "Monthly pay", "amount": 2500.00, "date": "2024-01-15"},
        {"type": "expense", "category": "Food", "description": "Groceries", "amount": 600.00, "date": "2024-01-16"},
        {"type": "expense", "category": "Food", "description": "Lunch", "amount": 200.00, "date": "2024-01-17"},
        {"type": "expense", "category": "Transport", "description": "Fuel", "amount": 200.00, "date": "2024-01-18"},
    ]

    report = view_by_category(transactions)

    assert "Food" in report
    assert "Transport" in report
    assert "₦ 800.00" in report
    assert "80.0%" in report
