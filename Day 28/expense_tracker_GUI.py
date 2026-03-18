import customtkinter as ctk
import csv
import os
from datetime import datetime

# file name
FILE_NAME = "expenses.csv"

# create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount"])

# function to add expense
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    if category == "" or amount == "":
        result_label.configure(text="Please fill all fields")
        return

    try:
        amount = float(amount)
    except:
        result_label.configure(text="Invalid amount")
        return

    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])

    result_label.configure(text="Expense added")

    category_entry.delete(0, "end")
    amount_entry.delete(0, "end")
    date_entry.delete(0, "end")

# function to show summary
def show_summary():
    summary = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            summary[cat] = summary.get(cat, 0) + amt

    output_box.delete("0.0", "end")

    for cat in summary:
        output_box.insert("end", f"{cat}: ${summary[cat]:.2f}\n")

# GUI setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("400x500")

# title
title = ctk.CTkLabel(app, text="Expense Tracker", font=("Arial", 20))
title.pack(pady=10)

# category
category_entry = ctk.CTkEntry(app, placeholder_text="Category")
category_entry.pack(pady=5)

# amount
amount_entry = ctk.CTkEntry(app, placeholder_text="Amount in USD (1.00)")
amount_entry.pack(pady=5)

# date
date_entry = ctk.CTkEntry(app, placeholder_text="Date (YYYY-MM-DD)")
date_entry.pack(pady=5)

# add button
add_btn = ctk.CTkButton(app, text="Add Expense", command=add_expense)
add_btn.pack(pady=10)

# summary button
summary_btn = ctk.CTkButton(app, text="Show Summary", command=show_summary)
summary_btn.pack(pady=5)

# result label
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=5)

# output box
output_box = ctk.CTkTextbox(app, height=200)
output_box.pack(pady=10, padx=10)

# run app
app.mainloop()