from utils import add_transaction, main_menu_text, view_all, get_summary, view_by_category


def main():
    print(main_menu_text())
    transactions = []

    while True:
        choice = input("> ")
        if choice == "1":
            transactions = add_transaction(transactions, "income")
            print("Income added.")
        elif choice == "2":
            transactions = add_transaction(transactions, "expense")
            print("Expense added.")
        elif choice == "3":
            view_all(transactions)
        elif choice == "4":
            print(get_summary(transactions))
        elif choice == "5":
            print(view_by_category(transactions))
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a number from the menu.")

        print(main_menu_text())


if __name__ == "__main__":
    main()
