# Expense Tracker (CLI + CSV)

A simple command-line expense tracker to help you keep track of your daily spending. You can add expenses, view them by category, and get a quick summary. All data is saved in a CSV file for easy access and backup.

## Features

- Add a new expense with **category, amount, and date**  
- View a summary of expenses by **category**  
- Simple command-line interface (CLI)  
- Saves all data in a **CSV file**  

## How It Works

1. **Add an expense** – Enter the category (like Food, Transport, Bills), the amount, and the date.  
2. **View summary** – See the total spent in each category.  
3. **CSV storage** – All expenses are stored in `expenses.csv`. You can open it in Excel or Google Sheets if needed.

## Example Usage

```bash
$ python expense_tracker.py
Welcome to Expense Tracker!

1. Add Expense
2. View Summary
3. Exit

Choose an option: 1

Enter category: Food
Enter amount: 12.5
Enter date (YYYY-MM-DD) [leave empty for today]: 
Expense added successfully!

Choose an option: 2

Expense Summary:
Food: $12.50
Transport: $8.00
Bills: $50.00
```

## How to Run

1. Make sure **Python 3** is installed.  
2. Download `expense_tracker.py` to a folder.  
3. Open terminal or command prompt in that folder.  
4. Run the script:

```bash
python expense_tracker.py