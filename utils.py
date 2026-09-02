import datetime


def main_menu_text():
    return """
===== BUDGET TRACKER =====
[1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category  [6] Exit
"""


def add_transaction(transactions, ttype):
    date = datetime.date.today().isoformat()

    if ttype == "income":
        source = input("Enter source: ")
        amount = float(input("Enter your amount: "))
        transactions.append(
            {
                "type": "income",
                "category": source,
                "description": f"Income from {source}",
                "amount": amount,
                "date": date,
            }
        )
        return transactions

    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    transactions.append(
        {
            "type": "expense",
            "category": category,
            "description": description,
            "amount": amount,
            "date": date,
        }
    )
    return transactions


def view_all(transactions):
    if len(transactions) == 0:
        print("No transactions yet")
        return

    print(f"{'Type':<8} {'Category':<15} {'Description':<20} {'Amount':>12} {'Date':<10}")
    print("-" * 80)
    for item in transactions:
        print(f"{item['type']:<8} {item['category']:<15} {item['description']:<20} {item['amount']:>12,.2f} {item['date']:<10}")


def get_summary(transactions):
    total_income = 0.0
    total_expenses = 0.0

    for item in transactions:
        if item["type"] == "income":
            total_income += item["amount"]
        elif item["type"] == "expense":
            total_expenses += item["amount"]

    total_amount = total_income - total_expenses

    return (
        "📊 FINANCIAL SUMMARY\n"
        "--------------------------\n"
        f"Total Income:    ₦ {total_income:,.2f}\n"
        f"Total Expenses:  ₦ {total_expenses:,.2f}\n"
        f"Net Balance:     ₦ {total_amount:,.2f}\n"
    )


def view_by_category(transactions):
    if not transactions:
        return "No transactions yet\n"

    category_totals = {}
    total_expenses = 0.0

    for item in transactions:
        if item["type"] == "expense":
            category_totals[item["category"]] = category_totals.get(item["category"], 0.0) + item["amount"]
            total_expenses += item["amount"]

    if not category_totals:
        return "📁 SPENDING BY CATEGORY\n--------------------------\nNo expenses recorded\n"

    result = "📁 SPENDING BY CATEGORY\n--------------------------\n"
    for category, total in category_totals.items():
        percentage = (total / total_expenses) * 100 if total_expenses else 0
        result += f"{category:<15} ₦ {total:,.2f}  ({percentage:.1f}%)\n"

    return result
