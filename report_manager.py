from collections import defaultdict
from expense_manager import load_expenses
from budget_manager import load_budgets


def spending_summary():
    expenses = load_expenses()

    print("\n--- Overall Spending Summary ---")
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)

    categories = defaultdict(float)
    months = defaultdict(float)

    for item in expenses:
        categories[item["category"]] += item["amount"]
        months[item["date"][:7]] += item["amount"]

    print(f"Number of expenses : {len(expenses)}")
    print(f"Total spending     : {total:.2f}")
    print(f"Average expense    : {average:.2f}")

    print("\nCategory totals:")
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:<22} {amount:>10.2f}")

    print("\nMonthly totals:")
    for month, amount in sorted(months.items()):
        print(f"  {month:<10} {amount:>10.2f}")


def monthly_report():
    expenses = load_expenses()
    budgets = load_budgets()

    month = input("Enter month (YYYY-MM): ").strip()
    month_expenses = [x for x in expenses if x["date"].startswith(month)]

    spent = sum(x["amount"] for x in month_expenses)
    budget = budgets.get(month)

    categories = defaultdict(float)
    for item in month_expenses:
        categories[item["category"]] += item["amount"]

    print(f"\n--- Monthly Spending Report: {month} ---")
    print(f"Transactions: {len(month_expenses)}")
    print(f"Total spent : {spent:.2f}")
    print(f"Budget      : {budget:.2f}" if budget is not None else "Budget      : Not set")

    if budget is not None:
        remaining = budget - spent
        print(f"Remaining   : {remaining:.2f}")
        if remaining < 0:
            print("Status      : Budget exceeded")
        else:
            print("Status      : Within budget")

    print("\nCategory breakdown:")
    if categories:
        for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / spent * 100) if spent else 0
            print(f"  {category:<22} {amount:>10.2f} ({percentage:>5.1f}%)")
    else:
        print("  No expenses recorded for this month.")
