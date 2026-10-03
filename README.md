# Personal Expense & Budget Tracker

A console-based Python application developed for the VEDA Technology internship task.

## Description

The Personal Expense & Budget Tracker allows users to record daily expenses, organize expenses by category, define monthly budgets, search/filter records, and generate spending summaries.

## Features

- Add expenses
- View all expenses
- Edit expenses
- Delete expenses
- Search expenses
- Filter by category
- Filter by month
- Category-wise spending summary
- Monthly spending summary
- Set monthly budgets
- Check budget status
- Overall spending report
- Monthly spending report
- JSON data storage
- Date validation
- Exception handling
- Input validation

## Technology

- Python 3
- JSON
- datetime
- collections
- Git
- GitHub
- VS Code / PyCharm

## Project Structure

```text
personal-expense-budget-tracker/
├── main.py
├── expense_manager.py
├── budget_manager.py
├── report_manager.py
├── utils.py
├── data/
│   ├── expenses.json
│   └── budgets.json
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

Open PowerShell/Command Prompt in the project folder:

```powershell
python main.py
```

If `python` is not recognized, try:

```powershell
py main.py
```

## Data Storage

Expense records are stored in:

```text
data/expenses.json
```

Monthly budgets are stored in:

```text
data/budgets.json
```

The files are created automatically if they do not exist.

## Example Workflow

1. Select `1. Expense Management`.
2. Add an expense.
3. View the expense list.
4. Set a monthly budget from `2. Budget Management`.
5. Check the budget status.
6. Open Reports to see category and monthly summaries.

## Validation

The application validates:

- Empty expense names/categories
- Positive amounts
- Date format: `YYYY-MM-DD`
- Month format: `YYYY-MM`
- Invalid menu choices
- Invalid numeric input
- Missing/corrupted JSON data

## GitHub

After testing locally, initialize Git and push the project to a GitHub repository.

Example:

```powershell
git init
git add .
git commit -m "Create Personal Expense and Budget Tracker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/personal-expense-budget-tracker.git
git push -u origin main
```
