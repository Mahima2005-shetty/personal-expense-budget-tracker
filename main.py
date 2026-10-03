from expense_manager import (
    add_expense, view_expenses, edit_expense, delete_expense,
    search_expenses, filter_expenses, category_summary, monthly_summary
)
from budget_manager import set_budget, view_budgets, check_budget
from report_manager import spending_summary, monthly_report
from utils import print_header, pause


def expense_menu():
    while True:
        print_header("EXPENSE MANAGEMENT")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("5. Search expenses")
        print("6. Filter expenses")
        print("7. Category-wise summary")
        print("8. Monthly summary")
        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            search_expenses()
        elif choice == "6":
            filter_expenses()
        elif choice == "7":
            category_summary()
        elif choice == "8":
            monthly_summary()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
        pause()


def budget_menu():
    while True:
        print_header("BUDGET MANAGEMENT")
        print("1. Set monthly budget")
        print("2. View budgets")
        print("3. Check budget status")
        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            set_budget()
        elif choice == "2":
            view_budgets()
        elif choice == "3":
            check_budget()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
        pause()


def reports_menu():
    while True:
        print_header("REPORTS")
        print("1. Overall spending summary")
        print("2. Monthly spending report")
        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            spending_summary()
        elif choice == "2":
            monthly_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
        pause()


def main():
    while True:
        print_header("VEDA TECHNOLOGY - PERSONAL EXPENSE & BUDGET TRACKER")
        print("1. Expense Management")
        print("2. Budget Management")
        print("3. Reports")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            expense_menu()
        elif choice == "2":
            budget_menu()
        elif choice == "3":
            reports_menu()
        elif choice == "0":
            print("\nThank you for using Personal Expense & Budget Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
