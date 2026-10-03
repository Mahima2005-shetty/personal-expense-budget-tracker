from datetime import datetime
from utils import (
    load_json, save_json, DATA_DIR, get_positive_float,
    get_date_input, get_month_input
)

EXPENSES_FILE = DATA_DIR / "expenses.json"


def load_expenses():
    return load_json(EXPENSES_FILE, [])


def save_expenses(expenses):
    save_json(EXPENSES_FILE, expenses)


def next_id(expenses):
    return max((item["id"] for item in expenses), default=0) + 1


def add_expense():
    expenses = load_expenses()

    print("\n--- Add Expense ---")
    title = input("Expense name: ").strip()
    while not title:
        print("Expense name cannot be empty.")
        title = input("Expense name: ").strip()

    category = input("Category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    amount = get_positive_float("Amount: ")
    date = get_date_input("Date (YYYY-MM-DD, press Enter for today): ", allow_blank=True)
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    note = input("Note (optional): ").strip()

    expense = {
        "id": next_id(expenses),
        "name": title,
        "category": category.title(),
        "amount": round(amount, 2),
        "date": date,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully with ID {expense['id']}.")


def print_expense_table(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 92)
    print(f"{'ID':<5}{'Date':<14}{'Name':<25}{'Category':<18}{'Amount':>12}{'Note':<15}")
    print("-" * 92)

    for item in expenses:
        note = item.get("note", "")
        print(
            f"{item['id']:<5}"
            f"{item['date']:<14}"
            f"{item['name'][:24]:<25}"
            f"{item['category'][:17]:<18}"
            f"{item['amount']:>12.2f}"
            f"{note[:14]:<15}"
        )

    print("-" * 92)
    print(f"Total: {sum(item['amount'] for item in expenses):.2f}")


def view_expenses():
    expenses = load_expenses()
    print_expense_table(expenses)


def find_expense(expenses, expense_id):
    return next((item for item in expenses if item["id"] == expense_id), None)


def edit_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses available to edit.")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter expense ID to edit: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    expense = find_expense(expenses, expense_id)
    if not expense:
        print("Expense not found.")
        return

    print("Press Enter to keep the current value.")

    name = input(f"Expense name [{expense['name']}]: ").strip()
    category = input(f"Category [{expense['category']}]: ").strip()
    amount_text = input(f"Amount [{expense['amount']:.2f}]: ").strip()
    date = input(f"Date [{expense['date']}]: ").strip()
    note = input(f"Note [{expense.get('note', '')}]: ").strip()

    if name:
        expense["name"] = name
    if category:
        expense["category"] = category.title()

    if amount_text:
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
            expense["amount"] = round(amount, 2)
        except ValueError:
            print("Invalid amount. Existing amount kept.")

    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            expense["date"] = date
        except ValueError:
            print("Invalid date. Existing date kept.")

    if note:
        expense["note"] = note

    save_expenses(expenses)
    print("Expense updated successfully.")


def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter expense ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    expense = find_expense(expenses, expense_id)
    if not expense:
        print("Expense not found.")
        return

    confirm = input(f"Delete '{expense['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        expenses.remove(expense)
        save_expenses(expenses)
        print("Expense deleted successfully.")
    else:
        print("Deletion cancelled.")


def search_expenses():
    expenses = load_expenses()
    keyword = input("Enter name/category/note to search: ").strip().lower()

    results = [
        item for item in expenses
        if keyword in item["name"].lower()
        or keyword in item["category"].lower()
        or keyword in item.get("note", "").lower()
    ]

    print_expense_table(results)


def filter_expenses():
    expenses = load_expenses()

    print("\n1. Filter by category")
    print("2. Filter by month (YYYY-MM)")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        category = input("Enter category: ").strip().lower()
        results = [x for x in expenses if x["category"].lower() == category]
    elif choice == "2":
        month = get_month_input("Enter month (YYYY-MM): ")
        results = [x for x in expenses if x["date"].startswith(month)]
    else:
        print("Invalid choice.")
        return

    print_expense_table(results)


def category_summary():
    expenses = load_expenses()
    totals = {}

    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0) + item["amount"]

    print("\n--- Category-wise Spending ---")
    if not totals:
        print("No expenses found.")
        return

    for category, total in sorted(totals.items()):
        print(f"{category:<25} {total:>10.2f}")


def monthly_summary():
    expenses = load_expenses()
    month = get_month_input("Enter month (YYYY-MM): ")

    results = [x for x in expenses if x["date"].startswith(month)]
    print(f"\n--- Monthly Summary: {month} ---")
    print_expense_table(results)
