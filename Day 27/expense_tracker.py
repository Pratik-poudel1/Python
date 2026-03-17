import csv
import os
from datetime import datetime

# CSV file to store expenses
CSV_FILE = "expenses.csv"

# Ensure the CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    category = input("Enter category: ").strip()
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    date_input = input("Enter date (YYYY-MM-DD) [leave empty for today]: ").strip()
    if date_input == "":
        date_input = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today.")
            date_input = datetime.today().strftime("%Y-%m-%d")
    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_input, category, amount])
    
    print("Expense added successfully!\n")

def view_summary():
    expenses = {}
    if not os.path.exists(CSV_FILE):
        print("No expenses found.\n")
        return

    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            expenses[cat] = expenses.get(cat, 0) + amt
    
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nExpense Summary:")
    for cat, amt in expenses.items():
        print(f"{cat}: ${amt:.2f}")
    print()

def main():
    print("Welcome to Expense Tracker!\n")
    while True:
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit\n")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()