from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = "data"
EXPENSE_FILE = os.path.join(DATA_DIR, "expenses.json")
BUDGET_FILE = os.path.join(DATA_DIR, "budgets.json")


def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []

    with open(EXPENSE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_expenses(expenses):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(EXPENSE_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def load_budgets():
    if not os.path.exists(BUDGET_FILE):
        return {}

    with open(BUDGET_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_budgets(budgets):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(BUDGET_FILE, "w", encoding="utf-8") as file:
        json.dump(budgets, file, indent=4)


@app.route("/")
def index():
    expenses = load_expenses()
    current_month = datetime.now().strftime("%Y-%m")

    monthly_expenses = [
        expense for expense in expenses
        if expense.get("date", "").startswith(current_month)
    ]

    total_spent = sum(
        float(expense.get("amount", 0))
        for expense in monthly_expenses
    )

    budgets = load_budgets()
    budget = float(budgets.get(current_month, 0))
    remaining = budget - total_spent if budget else 0

    categories = {}

    for expense in monthly_expenses:
        category = expense.get("category", "Other")
        amount = float(expense.get("amount", 0))

        categories[category] = (
            categories.get(category, 0) + amount
        )

    return render_template(
        "index.html",
        expenses=monthly_expenses,
        total_spent=total_spent,
        budget=budget,
        remaining=remaining,
        categories=categories,
        current_month=current_month
    )


@app.route("/expenses")
def expenses():
    all_expenses = load_expenses()

    return render_template(
        "expenses.html",
        expenses=all_expenses
    )


@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expenses = load_expenses()

        existing_ids = [
            int(expense.get("id", 0))
            for expense in expenses
            if str(expense.get("id", "")).isdigit()
        ]

        new_id = max(existing_ids, default=0) + 1

        expense = {
            "id": new_id,
            "name": request.form["name"],
            "category": request.form["category"],
            "amount": float(request.form["amount"]),
            "date": request.form["date"],
            "note": request.form.get("note", "")
        }

        expenses.append(expense)
        save_expenses(expenses)

        return redirect(url_for("expenses"))

    return render_template("add_expense.html")


@app.route("/edit-expense/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expenses = load_expenses()

    expense = next(
        (
            item for item in expenses
            if int(item.get("id", 0)) == expense_id
        ),
        None
    )

    if expense is None:
        return redirect(url_for("expenses"))

    if request.method == "POST":
        expense["name"] = request.form["name"]
        expense["category"] = request.form["category"]
        expense["amount"] = float(request.form["amount"])
        expense["date"] = request.form["date"]
        expense["note"] = request.form.get("note", "")

        save_expenses(expenses)

        return redirect(url_for("expenses"))

    return render_template(
        "edit_expense.html",
        expense=expense
    )


@app.route("/delete-expense/<int:expense_id>")
def delete_expense(expense_id):
    expenses = load_expenses()

    expenses = [
        expense for expense in expenses
        if int(expense.get("id", 0)) != expense_id
    ]

    save_expenses(expenses)

    return redirect(url_for("expenses"))


@app.route("/budget", methods=["GET", "POST"])
def budget():
    budgets = load_budgets()
    current_month = datetime.now().strftime("%Y-%m")

    if request.method == "POST":
        month = request.form["month"]
        amount = float(request.form["amount"])

        budgets[month] = amount
        save_budgets(budgets)

        return redirect(url_for("budget"))

    return render_template(
        "budget.html",
        budgets=budgets,
        current_month=current_month
    )


@app.route("/reports")
def reports():
    expenses = load_expenses()
    category_totals = {}

    for expense in expenses:
        category = expense.get("category", "Other")
        amount = float(expense.get("amount", 0))

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    total = sum(category_totals.values())

    return render_template(
        "reports.html",
        category_totals=category_totals,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)
