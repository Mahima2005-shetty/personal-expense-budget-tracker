from utils import load_json, save_json, DATA_DIR, get_month_input, get_positive_float
from expense_manager import load_expenses

BUDGETS_FILE = DATA_DIR / "budgets.json"


def load_budgets():
    return load_json(BUDGETS_FILE, {})


def save_budgets(budgets):
    save_json(BUDGETS_FILE, budgets)


def set_budget():
    budgets = load_budgets()
    month = get_month_input("Enter month (YYYY-MM): ")
    amount = get_positive_float("Monthly budget amount: ")

    budgets[month] = round(amount, 2)
    save_budgets(budgets)
    print(f"Budget for {month} saved successfully.")


def view_budgets():
    budgets = load_budgets()

    print("\n--- Monthly Budgets ---")
    if not budgets:
        print("No budgets found.")
        return

    for month in sorted(budgets):
        print(f"{month}: {budgets[month]:.2f}")


def check_budget():
    budgets = load_budgets()
    expenses = load_expenses()
    month = get_month_input("Enter month (YYYY-MM): ")

    budget = budgets.get(month)
    spent = sum(item["amount"] for item in expenses if item["date"].startswith(month))

    print(f"\n--- Budget Status: {month} ---")
    print(f"Budget : {budget:.2f}" if budget is not None else "Budget : Not set")
    print(f"Spent  : {spent:.2f}")

    if budget is None:
        print("Set a budget for this month to track remaining amount.")
        return

    remaining = budget - spent
    print(f"Remaining: {remaining:.2f}")

    if remaining < 0:
        print(f"Budget exceeded by {abs(remaining):.2f}.")
    elif remaining == 0:
        print("Budget fully used.")
    else:
        print("You are within the monthly budget.")
