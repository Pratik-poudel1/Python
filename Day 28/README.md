# Expense Tracker GUI (CustomTkinter)

This is a simple expense tracker with a graphical user interface (GUI) built using CustomTkinter. It allows you to add daily expenses and view a summary by category in a clean and easy way.

This project is a GUI version of the basic CLI expense tracker and is designed to be simple and beginner-friendly.

## Features

- Add expense with category, amount, and date  
- Automatically uses today’s date if not provided  
- View total expenses grouped by category  
- Simple and clean GUI using CustomTkinter  
- Data stored in a CSV file (`expenses.csv`)  

## How It Works

1. Enter the **category** (Food, Transport, Bills, etc.)  
2. Enter the **amount**  
3. Enter the **date** (or leave empty for today)  
4. Click **Add Expense** to save the data  
5. Click **Show Summary** to see total spending by category  

All data is saved in a CSV file, so you can open it later in Excel or Google Sheets.

## How to Run

1. Make sure Python 3 is installed  
2. Install CustomTkinter:

```bash
pip install customtkinter