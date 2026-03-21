# Gaming Gadget Store GUI

A Python desktop app I made for my 1st semester project. It's a simple store GUI where you can register, log in, pick gaming gadgets, and go through a full checkout with membership discounts, VAT, delivery, and ATM payment.

---

## What it does

- Register and login with basic validation
- Browse 30 gaming products with quantity controls
- Cart with item removal
- Checkout flow: gift wrap → membership → delivery → VAT → bill
- ATM payment with its own register/login
- Saves bill and payment records to text files
- Loyalty points at the end (just for fun)

---

## Setup

1. Clone the repo
2. Install dependencies:
```
pip install customtkinter pillow
```
3. Run it:
```
python Project.py
```

Make sure `myico.ico` and `side-img.png` are in the same folder as `Project.py`.

---

## Built with

- Python 3
- CustomTkinter
- Pillow
- SQLite3 (built-in)

---

## Notes

- Passwords are stored as plain text in SQLite. I know that's not great — hashing is something I'm learning next.
- The `users/` folder gets created automatically when you run the app. Bills and payment logs go there. That folder is in `.gitignore` so no personal data gets pushed.
- Prices are in Nepali Rupees (Rs.)

---

Made by a CSIT 1st semester student. It's not perfect but it works.
