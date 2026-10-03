import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def load_json(file_path, default):
    try:
        if not file_path.exists():
            save_json(file_path, default)
            return default

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {file_path.name}. Starting with empty/default data.")
        return default


def save_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        print(f"Error saving data: {error}")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive number.")


def get_date_input(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()

        if allow_blank and not value:
            return ""

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def get_month_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m")
            return value
        except ValueError:
            print("Invalid month. Use YYYY-MM.")


def print_header(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def pause():
    input("\nPress Enter to continue...")
