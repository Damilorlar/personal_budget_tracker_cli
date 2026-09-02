import datetime

transactions = []

def main_menu_text():
    return """
    ===== BUDGET TRACKER =====
    [1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category  [6] Exit
    """



def user_details(transactions, ttype):
    date = datetime.date.today().isoformat()
    category = input("Enter your category: ")
    amount = int(input("Enter your amount: "))
    transactions.append({"type": ttype, "category": category, "amount": amount, "date": date})
    return transactions




def view_all(transactions):
    if len(transactions) == 0:
        print("No transactions yet")
        return 

    for t in transactions:
        print(t["type"], t["category"], t["amount"], t["date"])


def get_summary(transactions):
    total_income = 0
    total_expenses = 0
    for t in transactions:
        if t["type"] == "income":
            total_income = total_income + t["amount"]
        if t["type"] == "expense":
            total_expenses = total_expenses + t["amount"]

    total_amount = total_income - total_expenses   # notice: minus, not plus — see below

    return f"""
      FINANCIAL SUMMARY
    --------------------------
    Total Income = ₦{total_income}
    Total Expenses = ₦{total_expenses}
    Net Balance = ₦{total_amount}
    """

def view_by_category(transactions):
    if len(transactions) == 0:
        print("No transactions yet")
        return

    expense_totals = {}
    income_totals = {}

    for t in transactions:
        if t["type"] == "expense":
            cat = t["category"]
            expense_totals[cat] = expense_totals.get(cat, 0) + t["amount"]
        if t["type"] == "income":
            cat = t["category"]
            income_totals[cat] = income_totals.get(cat, 0) + t["amount"]

    result = "SPENDING BY CATEGORY (EXPENSES)\n--------------------------\n"
    for n, v in expense_totals.items():
        result += f"{n}: ₦{v}\n"

    result += "\nINCOME BY CATEGORY\n--------------------------\n"
    for n, v in income_totals.items():
        result += f"{n}: ₦{v}\n"

    return result