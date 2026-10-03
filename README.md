# Personal Expense & Budget Tracker

A Python-based Personal Expense & Budget Tracker with both a command-line interface and a Flask web application.

## Project Overview

The Personal Expense & Budget Tracker helps users record, organize, and analyze their daily expenses.

The application provides expense management, category-wise tracking, monthly budgets, search and filtering, and spending reports.

## Features

### Expense Management

- Add new expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Store expense details such as:
  - Expense name
  - Category
  - Amount
  - Date
  - Notes

### Search & Filtering

- Search expenses by name
- Search by category
- Search by notes
- Filter expenses by category

### Budget Management

- Set a monthly budget
- Store budgets by month
- Calculate total monthly spending
- Calculate remaining budget

### Reports

- Category-wise spending summary
- Total spending calculation
- Monthly spending information

### Data Storage

The application uses JSON files for persistent data storage.

```text
data/
├── expenses.json
└── budgets.json
Web Application

The project includes a Flask-based web interface.

Main web pages:

Dashboard
Expenses
Add Expense
Edit Expense
Budget
Reports
Technology Stack
Backend
Python
Flask
Frontend
HTML
CSS
Jinja2 Templates
Data Storage
JSON
Development Tools
Git
GitHub
Visual Studio Code / Notepad
PowerShell
Project Structure
personal-expense-budget-tracker/
│
├── app.py
├── main.py
├── expense_manager.py
├── budget_manager.py
├── report_manager.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── sample_output.txt
│
├── data/
│   ├── expenses.json
│   └── budgets.json
│
└── templates/
    ├── index.html
    ├── expenses.html
    ├── add_expense.html
    ├── edit_expense.html
    ├── budget.html
    └── reports.html
Installation

Clone the repository:

git clone https://github.com/Mahima2005-shetty/personal-expense-budget-tracker.git

Move into the project directory:

cd personal-expense-budget-tracker

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
Run the Console Application

Run:

python main.py
Run the Web Application

Run:

python app.py

The Flask application will start at:

http://127.0.0.1:5000

Open the address in a web browser.

Example Expense Data
{
    "id": 1,
    "name": "Groceries",
    "category": "Food",
    "amount": 2500,
    "date": "2026-10-01",
    "note": "Monthly groceries"
}
Example Budget
{
    "2026-10": 10000
}
Learning Outcomes

This project demonstrates the use of:

Python functions
Lists and dictionaries
File handling
JSON data processing
CSV/JSON concepts
Date and time handling
Exception handling
Input validation
Flask routing
HTML templates
CRUD operations
Search and filtering
Git and GitHub
Future Enhancements

Possible future improvements include:

User authentication
SQLite/MySQL database
Interactive charts
Export reports to CSV/PDF
Advanced date-range filtering
Responsive mobile interface
REST API support
Author

Mahima

Repository

GitHub:

https://github.com/Mahima2005-shetty/personal-expense-budget-tracker
