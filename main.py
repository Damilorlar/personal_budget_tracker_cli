from utils import main_menu_text, user_details, view_all,get_summary,view_by_category

print(main_menu_text())

transactions = []

# details = user_details()
# transactions = view_all

while True:
    choice = input(">")
    if choice == "1":
        detail = user_details(transactions, "income")
        print(detail)
    elif choice == "2":
        detail = user_details(transactions, "expense")
        print(detail)
    elif choice == "3":
       view_all(transactions)
    elif choice == "4":
       summary = get_summary(transactions)
       print(summary)
    elif choice == "5":
       category=view_by_category(transactions)
       print(category)

    elif choice == "6":
      break  