# Personal Budget Tracker CLI

A simple Python command-line application for tracking personal income and expenses. The app lets you add transactions, review all recorded entries, view a summary of totals, and see spending broken down by category.

## What the project does

This project currently provides an interactive menu-driven interface for:

- Adding income entries
- Adding expense entries
- Viewing all recorded transactions
- Seeing total income, total expenses, and net balance
- Viewing spending totals by expense category

## Current implementation status

This version is a lightweight in-memory budget tracker. It does not currently persist data to a database or file, so transactions are lost when the program exits.

## Requirements

- Python 3.10+

## Installation

```bash
git clone https://github.com/Damilorlar/personal_budget_tracker_cli.git
cd personal_budget_tracker_cli
python main.py
```

## Usage

Run the app:

```bash
python main.py
```

You will see a menu like this:

```text
===== BUDGET TRACKER =====
[1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category  [6] Exit
```

Then enter a number from the list:

- `1`: Add an income transaction
- `2`: Add an expense transaction
- `3`: View all recorded transactions
- `4`: Show financial summary
- `5`: Show spending grouped by category
- `6`: Exit the application

### Example session

```text
> 1
Enter your category: Salary
Enter your amount: 2500
> 2
Enter your category: Rent
Enter your amount: 900
> 4

      FINANCIAL SUMMARY
    --------------------------
    Total Income = ₦2500
    Total Expenses = ₦900
    Net Balance = ₦1600
```

## Data behavior

Each transaction stores:

- type: `income` or `expense`
- category
- amount
- date

The app uses a Python list in memory to hold transactions while the program is running.

## Project structure

```text
personal_budget_tracker_cli/
├── main.py
├── utils.py
├── README.md
```

## Notes

- The app is intentionally minimal and does not include authentication, user accounts, or multi-file storage.
- The summary is calculated from the current in-memory transaction list.
- Expense category analysis only includes expense transactions.

## Development

There are no automated tests in the current repository, so the project is best validated by running the app interactively and checking menu behavior manually.

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
