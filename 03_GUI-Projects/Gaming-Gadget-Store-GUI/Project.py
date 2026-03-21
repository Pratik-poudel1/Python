from customtkinter import *
from PIL import Image
import sqlite3
import os
import re
from tkinter import messagebox
import threading
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists('users'):
    os.makedirs('users')

conn = sqlite3.connect('users/shopdata.sqlite3')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()


atm_conn = sqlite3.connect('users/shopdata.sqlite3')
atm_cursor = atm_conn.cursor()
atm_cursor.execute('''
CREATE TABLE IF NOT EXISTS atm_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number TEXT NOT NULL,
    pin TEXT NOT NULL
)
''')

atm_conn.commit()

app = CTk()
app.title("Gaming Equipment Store")
width = 600
height = 480
screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()
centre_x = int(screen_w / 2 - width / 2)
centre_y = int(screen_h / 2 - height / 2)
app.geometry(f'{width}x{height}+{centre_x}+{centre_y}')
app.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))


set_appearance_mode("light")
set_default_color_theme("blue")
register_open = False
cart = []

gadgets = {
    '1': ('Gaming Mouse', 2500),
    '2': ('Mechanical Keyboard', 5000),
    '3': ('Gaming Headset', 3500),
    '4': ('Gaming Chair', 15000),
    '5': ('Gaming Card', 45000),
    '6': ('RGB Mousepad', 1500),
    '7': ('Gaming Monitor', 30000),
    '8': ('VR Headset', 40000),
    '9': ('Streaming Mic', 6000),
    '10': ('Gaming Desk', 20000),
    '11': ('Capture Card', 12000),
    '12': ('Gaming Controller', 7000),
    '13': ('Webcam', 5000),
    '14': ('Headphone Stand', 1200),
    '15': ('Cable Management Kit', 800),
    '16': ('Gaming Laptop', 120000),
    '17': ('Gaming Smartphone', 90000),
    '18': ('Graphics Card', 85000),
    '19': ('Gaming Router', 7000),
    '20': ('Gamepad', 3500),
    '21': ('Gaming Speakers', 8000),
    '22': ('LED Strip Lights', 1000),
    '23': ('Gaming Backpack', 3500),
    '24': ('Monitor Arm', 4000),
    '25': ('USB Hub', 1200),
    '26': ('Gaming Mouse Bungee', 900),
    '27': ('Microphone Arm', 1500),
    '28': ('Streaming Camera', 10000),
    '29': ('Gaming Glasses', 2000),
    '30': ('Gaming Mat', 1800)
}


try:
    side_img = CTkImage(Image.open(os.path.join(BASE_DIR, 'side-img.png')), size=(300, height))
    side_img_label = CTkLabel(app, image=side_img, text="")
    side_img_label.pack(expand=True, side="left")
except Exception:
    side_img_label = None


container = CTkFrame(app, width=width - 300, height=height, fg_color="#ffffff")
container.pack_propagate(0)
container.pack(expand=True, side="right")


register_frame = CTkFrame(container, fg_color="#ffffff")

CTkLabel(register_frame, text="Register", font=("Arial Bold", 24), text_color="#601E88").pack(pady=(30, 5))
reg_username = CTkEntry(register_frame, width=275, placeholder_text="Username")
reg_username.pack(pady=8)
reg_email = CTkEntry(register_frame, width=275, placeholder_text="Email")
reg_email.pack(pady=8)
reg_password = CTkEntry(register_frame, width=275, placeholder_text="Password", show="*")
reg_password.pack(pady=8)
reg_confirm = CTkEntry(register_frame, width=275, placeholder_text="Confirm Password", show="*")
reg_confirm.pack(pady=8)

def toggle_reg_pw():
    if reg_password.cget("show") == "*":
        reg_password.configure(show="")
        reg_confirm.configure(show="")
    else:
        reg_password.configure(show="*")
        reg_confirm.configure(show="*")

CTkSwitch(register_frame, text="Show Password", command=toggle_reg_pw).pack(pady=5)

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def switch_frame(show, hide):
    global register_open
    if show == register_frame:
        if register_open:
            return
        register_open = True
    elif show == login_frame:
        register_open = False
    hide.pack_forget()
    show.pack(expand=True, fill="both")

def handle_register():
    username = reg_username.get()
    email = reg_email.get()
    password = reg_password.get()
    confirm = reg_confirm.get()

    if len(username) < 8 or " " in username or any(c in username for c in "@#%&*!$"):
        messagebox.showerror("Error", "Username must be at least 8 characters with no spaces or special characters.")
        return
    if not is_valid_email(email):
        messagebox.showerror("Error", "Enter a valid email address.")
        return
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    if (len(password) < 6 or " " in password or
        not any(c.isdigit() for c in password) or
        not any(c.isupper() for c in password)):
        messagebox.showerror("Error", "Password must be at least 6 chars, include uppercase and numbers, and no spaces.")
        return

    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        messagebox.showinfo("Success", "Registered successfully! Please login.")
        switch_frame(login_frame, register_frame)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username or Email already exists.")

CTkButton(register_frame, text="Register", command=handle_register, fg_color="#601E88", text_color="white", width=275).pack(pady=15)
CTkLabel(register_frame, text="Already have an account?").pack()
CTkButton(register_frame, text="Login", command=lambda: switch_frame(login_frame, register_frame),
          fg_color="#EEEEEE", hover_color="#DDDDDD", text_color="#601E88", width=275).pack(pady=5)


login_frame = CTkFrame(container, fg_color="#ffffff")
login_frame.pack(expand=True, fill="both")
CTkLabel(login_frame, text="Login", font=("Arial Bold", 24), text_color="#601E88").pack(pady=(40, 10))
login_username = CTkEntry(login_frame, width=275, placeholder_text="Username")
login_username.pack(pady=10)
login_password = CTkEntry(login_frame, width=275, placeholder_text="Password", show="*")
login_password.pack(pady=10)

def toggle_login_pw():
    if login_password.cget("show") == "*":
        login_password.configure(show="")
    else:
        login_password.configure(show="*")

CTkSwitch(login_frame, text="Show Password", command=toggle_login_pw).pack()

def handle_login():
    u = login_username.get()
    p = login_password.get()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (u, p))
    if cursor.fetchone():
        messagebox.showinfo("Success", f"Welcome {u}!")
        login_frame.pack_forget()
        register_frame.pack_forget()
        container.pack_forget()
        if side_img_label:
            side_img_label.pack_forget()
        store_frame.pack(expand=True, fill="both")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

CTkButton(login_frame, text="Login", command=handle_login, fg_color="#601E88", text_color="white", width=275).pack(pady=20)
CTkLabel(login_frame, text="Don't have an account?").pack()
CTkButton(login_frame, text="Create Account", command=lambda: switch_frame(register_frame, login_frame),
          fg_color="#EEEEEE", hover_color="#DDDDDD", text_color="#601E88", width=275).pack(pady=5)


register_frame.pack_forget()
store_frame = CTkFrame(app, fg_color="#ffffff")
store_frame.pack_forget()
login_frame.pack(expand=True, fill="both")




CTkLabel(store_frame, text="Available Gadgets", font=("Arial Bold", 22), pady=10).pack()

scrollable_frame = CTkScrollableFrame(store_frame, width=width - 40, height=350)
scrollable_frame.pack(padx=10, pady=10, fill="both")

qty_vars = {}

def increase(k):
    val = int(qty_vars[k].get())
    if val < 50:
        qty_vars[k].set(str(val + 1))

def decrease(k):
    val = int(qty_vars[k].get())
    if val > 0:
        qty_vars[k].set(str(val - 1))

for key, (name, price) in gadgets.items():
    frame = CTkFrame(scrollable_frame, fg_color="#f0f0f0")
    frame.pack(fill="x", padx=5, pady=5)

    CTkLabel(frame, text=f"{key}. {name}", width=20, anchor="w").pack(side="left", padx=5)

    qty_var = StringVar(value="0")
    qty_vars[key] = qty_var

    qty_entry = CTkEntry(frame, width=35, height=25, textvariable=qty_var, justify="center", state="readonly")
    qty_entry.pack(side="right", padx=5)

    btn_inc = CTkButton(frame, text="▲", width=25, height=18, command=lambda k=key: increase(k))
    btn_inc.pack(side="right", padx=(0,2))
    btn_dec = CTkButton(frame, text="▼", width=25, height=18, command=lambda k=key: decrease(k))
    btn_dec.pack(side="right")

    
    price_label = CTkLabel(frame, text=f"Rs. {price} ", width=12, anchor="e")
    price_label.pack(side="right", padx=(5, 0))

button_frame = CTkFrame(store_frame, fg_color="transparent")
button_frame.pack(pady=10)

def add_to_cart():
    cart.clear()
    total_price = 0
    for k, qty_var in qty_vars.items():
        qty = int(qty_var.get())
        if qty > 0:
            name, price = gadgets[k]
            item_total = price * qty
            cart.append((name, qty, price, item_total))
            total_price += item_total
    if cart:
        messagebox.showinfo("Cart Updated", f"{len(cart)} items added to cart.\nTotal: Rs. {total_price}")
    else:
        messagebox.showinfo("Cart Empty", "No items selected.")

def show_cart():
    if not cart:
        messagebox.showinfo("Cart", "Your cart is empty.")
        return

    cart_win = CTkToplevel(store_frame)
    cart_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
    cart_win.title("Your Cart")
    cart_win.geometry(f"420x560+{centre_x}+{centre_y}")
    cart_win.lift()
    cart_win.attributes("-topmost", True)
    cart_win.after(10, lambda: cart_win.attributes("-topmost", False))

    CTkLabel(cart_win, text="🛒 Your Shopping Cart", font=("Arial Bold", 18)).pack(pady=10)

    cart_list_frame = CTkScrollableFrame(cart_win, width=380, height=280)
    cart_list_frame.pack(padx=10, pady=5)

    def refresh_cart_view():
        for widget in cart_list_frame.winfo_children():
            widget.destroy()

        for i, item in enumerate(cart):
            name, qty, price, item_total = item
            item_frame = CTkFrame(cart_list_frame, fg_color="#f9f9f9")
            item_frame.pack(fill="x", padx=5, pady=3)

            CTkLabel(item_frame, text=f"{name} x{qty} = Rs.{item_total}", anchor="w").pack(side="left", padx=5)
            CTkButton(item_frame, text="Remove", width=60, height=24,
                      command=lambda index=i: remove_from_cart(index)).pack(side="right", padx=5)

    def remove_from_cart(index):
        del cart[index]
        refresh_cart_view()

    refresh_cart_view()

    
    gift_wrap_charge = 0
    membership_discount_amt = 0
    membership_fee = 0
    membership_type = ""
    vat_amount = 0
    delivery_charge = 0
    loyalty_points = 0

    total = sum(item[3] for item in cart)



    def proceed_to_delivery(dis_total):
        del_win = CTkToplevel(cart_win)
        del_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
        del_win.title("Delivery Charges")
        del_win.geometry(f"400x280+{centre_x}+{centre_y}")
        del_win.lift()
        del_win.attributes("-topmost", True)
        del_win.after(10, lambda: del_win.attributes("-topmost", False))

        CTkLabel(del_win, text="Choose Delivery Option", font=("Arial", 16)).pack(pady=10)

        del_var = IntVar(value=0)  

        CTkRadioButton(del_win, text="Home Delivery - Rs. 500", variable=del_var, value=1).pack(anchor="w", padx=20)
        CTkRadioButton(del_win, text="Pickup (No Charge)", variable=del_var, value=2).pack(anchor="w", padx=20)

        def confirm_delivery():
            nonlocal delivery_charge
            choice = del_var.get()
            if choice == 1:
                delivery_charge = 500
            elif choice == 2:
                delivery_charge = 0
            else:
                messagebox.showerror("Error", "Please select a delivery option.")
                return
            del_win.destroy()
            proceed_to_vat(dis_total)

        CTkButton(del_win, text="Confirm", command=confirm_delivery, fg_color="#601E88", text_color="white").pack(pady=20)

    def proceed_to_vat(dis_total):
        vat_win = CTkToplevel(cart_win)
        vat_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
        vat_win.title("Select VAT Location")
        vat_win.geometry(f"350x220+{centre_x}+{centre_y}")
        vat_win.lift()
        vat_win.attributes("-topmost", True)
        vat_win.after(10, lambda: vat_win.attributes("-topmost", False))

        vat_var = IntVar(value=0)

        CTkLabel(vat_win, text="Select your location for VAT", font=("Arial", 16)).pack(pady=10)
        CTkRadioButton(vat_win, text="Inside Kathmandu - 13% V.A.T", variable=vat_var, value=13).pack(anchor="w", padx=20)
        CTkRadioButton(vat_win, text="Outside Kathmandu - 15% V.A.T", variable=vat_var, value=15).pack(anchor="w", padx=20)

        def vat_confirm():
            nonlocal vat_amount
            vat_percent = vat_var.get()
            vat_amount = dis_total * (vat_percent / 100)
            vat_win.destroy()
            show_final_bill(dis_total, vat_amount)

        CTkButton(vat_win, text="Confirm", command=vat_confirm, fg_color="#601E88", text_color="white").pack(pady=20)

    def show_final_bill(dis_total, vat_amt):
        nonlocal membership_discount_amt, gift_wrap_charge, membership_fee, membership_type, loyalty_points, delivery_charge

        grand_total = dis_total + vat_amt + gift_wrap_charge + membership_fee + delivery_charge
        loyalty_points = int(grand_total // 100)

        bill_win = CTkToplevel(cart_win)
        bill_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
        bill_win.title("Final Bill")
        bill_win.geometry(f"450x620+{centre_x}+{centre_y}")
        bill_win.lift()
        bill_win.attributes("-topmost", True)
        bill_win.after(10, lambda: bill_win.attributes("-topmost", False))

        CTkLabel(bill_win, text="=== Gadget Gaming Store BILL ===", font=("Arial Bold", 18), pady=10).pack()

        bill_text_frame = CTkScrollableFrame(bill_win, width=420, height=350)
        bill_text_frame.pack(padx=10, pady=5)

        CTkLabel(bill_text_frame, text=f"Username: {login_username.get()}", anchor="w").pack(pady=5)

        CTkLabel(bill_text_frame, text="Items Purchased:", anchor="w", font=("Arial", 14, "underline")).pack(anchor="w")

        for name, qty, price, total_price in cart:
            CTkLabel(bill_text_frame, text=f"- {name:25} Qty: {qty:2} x Rs.{price} = Rs.{total_price}", anchor="w").pack(anchor="w")

        CTkLabel(bill_text_frame, text=f"\nTotal Price: Rs. {total}", anchor="w").pack(pady=5)
        CTkLabel(bill_text_frame, text=f"Membership Discount: Rs. {membership_discount_amt}", anchor="w").pack(pady=5)
        if membership_fee > 0:
            CTkLabel(bill_text_frame, text=f"Membership Type: {membership_type} (Rs. {membership_fee})", anchor="w").pack(pady=5)
        CTkLabel(bill_text_frame, text=f"VAT (Tax) Amount: Rs. {vat_amt:.2f}", anchor="w").pack(pady=5)
        CTkLabel(bill_text_frame, text=f"Gift Wrap Charges: Rs. {gift_wrap_charge}", anchor="w").pack(pady=5)
        CTkLabel(bill_text_frame, text=f"Delivery Charges: Rs. {delivery_charge}", anchor="w").pack(pady=5)

        CTkLabel(bill_text_frame, text="------------------------------------------", anchor="w").pack(pady=5)
        CTkLabel(bill_text_frame, text=f"GRAND TOTAL: Rs. {grand_total:.2f}", anchor="w", font=("Arial Bold", 16)).pack(pady=5)

        
        from itertools import cycle
        import math
        loyalty_label = CTkLabel(bill_win, text="Loyalty Points Earned: 0", font=("Arial Bold", 14))
        loyalty_label.pack(pady=15)

        
        try:
            from customtkinter import CTkProgressBar
            progress = CTkProgressBar(bill_win, width=220, height=16)
            progress.set(0)
            progress.pack(pady=5)
        except Exception:
            progress = None

        def animate_points():
            for i in range(loyalty_points + 1):
                loyalty_label.configure(text=f"Loyalty Points Earned: {i}", text_color="#601E88")
                if progress:
                    progress.set(i / max(1, loyalty_points))
                
                size = 14 + int(4 * math.sin(i / max(1, loyalty_points) * math.pi))
                loyalty_label.configure(font=("Arial Bold", size))
                bill_win.update_idletasks()
                time.sleep(0.01)
            
            loyalty_label.configure(text_color="#601E88", font=("Arial Bold", 14))
            if progress:
                progress.set(1)

        threading.Thread(target=animate_points, daemon=True).start()

        def save_bill():
            with open('users/record.txt', 'a') as handle:
                handle.write('\n\n================ Gadget Gaming Store BILL ================\n')
                handle.write(f'Username : {login_username.get()}\n')
                handle.write('Items Purchased:\n')
                for name, qty, price, total_price in cart:
                    handle.write(f'- {name:25} Qty: {qty:2} x Rs.{price} = Rs.{total_price}\n')
                handle.write(f'\nTotal Price                  : Rs. {total}\n')
                handle.write(f'Membership Discount (Rs)     : Rs. {membership_discount_amt}\n')
                if membership_fee > 0:
                    handle.write(f'Membership Type              : {membership_type} (Rs. {membership_fee})\n')
                handle.write(f'Tax Amount (VAT)             : Rs. {vat_amt:.2f}\n')
                handle.write(f'Gift Wrap Charges            : Rs. {gift_wrap_charge}\n')
                handle.write(f'Delivery Charges             : Rs. {delivery_charge}\n')
                handle.write('----------------------------------------------------------\n')
                handle.write(f'GRAND TOTAL                  : Rs. {grand_total:.2f}\n')
                handle.write(f'Loyalty Points Earned        : {loyalty_points}\n')
                handle.write('==========================================================\n')
            messagebox.showinfo("Success", "Bill saved successfully!")

        def open_payment_window():
            pay_win = CTkToplevel(bill_win)
            pay_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
            pay_win.title("Choose Payment Method")
            pay_win.geometry(f"400x300+{centre_x}+{centre_y}")
            pay_win.lift()
            pay_win.attributes("-topmost", True)
            pay_win.after(10, lambda: pay_win.attributes("-topmost", False))

            CTkLabel(pay_win, text="Select Payment Method", font=("Arial", 16)).pack(pady=10)
            payment_var = IntVar(value=0)

            CTkRadioButton(pay_win, text="ATM/Card", variable=payment_var, value=1).pack(anchor="w", padx=20)
            CTkRadioButton(pay_win, text="Cash on Delivery", variable=payment_var, value=2).pack(anchor="w", padx=20)

            def confirm_payment():
                method = payment_var.get()
                if method == 1:
                    pay_win.destroy()
                    open_atm_payment(grand_total)
                elif method == 2:
                    pay_win.destroy()
                    messagebox.showinfo("Payment", "Cash on Delivery selected. Please pay when delivered.")
                else:
                    messagebox.showerror("Error", "Please select a payment method.")

            CTkButton(pay_win, text="Confirm Payment Method", command=confirm_payment,
                    fg_color="#601E88", text_color="white").pack(pady=20)

        def open_atm_payment(amount):
            atm_win = CTkToplevel(store_frame)
            atm_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
            atm_win.title("ATM Payment")
            atm_win.geometry(f"420x460+{centre_x}+{centre_y}")
            atm_win.lift()
            atm_win.attributes("-topmost", True)
            atm_win.after(10, lambda: atm_win.attributes("-topmost", False))
            
            
            atm_container = CTkFrame(atm_win, fg_color="#ffffff")
            atm_container.pack(fill="both", expand=True, padx=20, pady=20)
            
            
            atm_register_frame = CTkFrame(atm_container, fg_color="#ffffff")
            
            CTkLabel(atm_register_frame, text="ATM Register", font=("Arial Bold", 18)).pack(pady=(20, 10))
            reg_card_entry = CTkEntry(atm_register_frame, width=250, placeholder_text="6-digit Card Number")
            reg_card_entry.pack(pady=5)
            reg_pin_entry = CTkEntry(atm_register_frame, width=250, placeholder_text="PIN", show="*")
            reg_pin_entry.pack(pady=5)
            reg_confirm_pin_entry = CTkEntry(atm_register_frame, width=250, placeholder_text="Confirm PIN", show="*")
            reg_confirm_pin_entry.pack(pady=5)
            
            def register_user():
                card = reg_card_entry.get().strip()
                pin = reg_pin_entry.get().strip()
                confirm = reg_confirm_pin_entry.get().strip()

                if len(card) != 6 or not card.isdigit():
                    messagebox.showerror("Error", "Card number must be exactly 6 digits.")
                    return

                if len(pin) != 4 or not pin.isdigit():
                    messagebox.showerror("Error", "PIN must be exactly 4 digits.")
                    return

                if pin != confirm:
                    messagebox.showerror("Error", "PINs do not match.")
                    return

                try:
                    atm_cursor.execute("INSERT INTO atm_users (card_number, pin) VALUES (?, ?)", (card, pin))
                    atm_conn.commit()
                    messagebox.showinfo("Success", "ATM account registered successfully!")
                    switch_atm_frame(atm_login_frame, atm_register_frame)
                    
                    login_card_entry.delete(0, END)
                    login_card_entry.insert(0, card)
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Card number already exists.")
            
            CTkButton(atm_register_frame, text="Register", command=register_user, 
                    fg_color="#601E88", text_color="white", width=250).pack(pady=15)
            
            CTkLabel(atm_register_frame, text="Already have an account?").pack()
            CTkButton(atm_register_frame, text="Login", 
                    command=lambda: switch_atm_frame(atm_login_frame, atm_register_frame),
                    fg_color="#EEEEEE", hover_color="#DDDDDD", text_color="#601E88", width=250).pack(pady=5)
            
            
            atm_login_frame = CTkFrame(atm_container, fg_color="#ffffff")
            
            CTkLabel(atm_login_frame, text="ATM Login", font=("Arial Bold", 18)).pack(pady=(20, 10))
            login_card_entry = CTkEntry(atm_login_frame, width=250, placeholder_text="6-digit Card Number")
            login_card_entry.pack(pady=10)
            login_pin_entry = CTkEntry(atm_login_frame, width=250, placeholder_text="PIN", show="*")
            login_pin_entry.pack(pady=10)
            
            def toggle_atm_pw():
                if login_pin_entry.cget("show") == "*":
                    login_pin_entry.configure(show="")
                else:
                    login_pin_entry.configure(show="*")
            
            CTkSwitch(atm_login_frame, text="Show PIN", command=toggle_atm_pw).pack()
            
            def login_user():
                card = login_card_entry.get().strip()
                pin = login_pin_entry.get().strip()
                atm_cursor.execute("SELECT * FROM atm_users WHERE card_number = ? AND pin = ?", (card, pin))
                user = atm_cursor.fetchone()
                if user:
                    messagebox.showinfo("Success", "Login successful!")
                    atm_win.destroy()
                    show_payment_bill_gui(card)
                else:
                    messagebox.showerror("Error", "Invalid card or PIN.")
            
            CTkButton(atm_login_frame, text="Login", command=login_user, 
                    fg_color="#601E88", text_color="white", width=250).pack(pady=20)
            
            CTkLabel(atm_login_frame, text="Don't have an account?").pack()
            CTkButton(atm_login_frame, text="Create Account", 
                    command=lambda: switch_atm_frame(atm_register_frame, atm_login_frame),
                    fg_color="#EEEEEE", hover_color="#DDDDDD", text_color="#601E88", width=250).pack(pady=5)
            
            
            def switch_atm_frame(show, hide):
                hide.pack_forget()
                show.pack(expand=True, fill="both")
            
            
            atm_register_frame.pack_forget()
            atm_login_frame.pack(expand=True, fill="both")

            def show_payment_bill_gui(card):
                pb_win = CTkToplevel(store_frame)
                pb_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
                pb_win.title("ATM Payment Bill")
                pb_win.geometry(f"420x350+{centre_x}+{centre_y}")
                pb_win.lift()
                pb_win.attributes("-topmost", True)
                pb_win.after(10, lambda: pb_win.attributes("-topmost", False))

                CTkLabel(pb_win, text="🧾 ATM Payment Successful", font=("Arial Bold", 18)).pack(pady=10)
                CTkLabel(pb_win, text=f"Username: {login_username.get()}").pack(pady=5)
                CTkLabel(pb_win, text=f"Card Used: {card}").pack(pady=5)
                CTkLabel(pb_win, text=f"Amount Paid: Rs. {amount}").pack(pady=5)
                CTkLabel(pb_win, text=f"Time: {time.ctime()}").pack(pady=5)

                with open("users/payment_log.txt", "a") as f:
                    f.write(f"User: {login_username.get()} | Paid: Rs. {amount} | Card: {card} | Time: {time.ctime()}\n")

                CTkButton(pb_win, text="Close", command=pb_win.destroy, fg_color="#cccccc", text_color="#000000").pack(pady=20)


        CTkButton(bill_win, text="Save Bill", command=save_bill, fg_color="#601E88", text_color="white", width=160).pack(pady=10)
        CTkButton(bill_win, text="Pay Now", command=open_payment_window,
                fg_color="#00a86b", text_color="white", width=160).pack(pady=5)
        CTkButton(bill_win, text="Close", command=bill_win.destroy, fg_color="#cccccc", text_color="#000000", width=160).pack()


    def proceed_to_membership(wrap_charge):
        nonlocal gift_wrap_charge, membership_discount_amt, membership_fee, membership_type
        gift_wrap_charge = wrap_charge

        mem_win = CTkToplevel(cart_win)
        mem_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
        mem_win.title("Membership Options")
        mem_win.geometry(f"400x320+{centre_x}+{centre_y}")
        mem_win.lift()
        mem_win.attributes("-topmost", True)
        mem_win.after(10, lambda: mem_win.attributes("-topmost", False))

        CTkLabel(mem_win, text="Are you a Member of our shop?", font=("Arial", 16)).pack(pady=10)
        mem_var = IntVar(value=0)

        CTkRadioButton(mem_win, text="Yes", variable=mem_var, value=1).pack(anchor="w", padx=20)
        CTkRadioButton(mem_win, text="No", variable=mem_var, value=2).pack(anchor="w", padx=20)

        def on_next():
            val = mem_var.get()
            if val == 1:
                def member_type_win():
                    mt_win = CTkToplevel(mem_win)
                    mt_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
                    mt_win.title("Select Membership Type")
                    mt_win.geometry(f"400x280+{centre_x}+{centre_y}")
                    mt_win.lift()
                    mt_win.attributes("-topmost", True)
                    mt_win.after(10, lambda: mt_win.attributes("-topmost", False))

                    CTkLabel(mt_win, text="Which member are you?", font=("Arial", 14)).pack(pady=10)
                    member_type_var = IntVar(value=0)

                    CTkRadioButton(mt_win, text="Platinum Member - 25% Discount", variable=member_type_var, value=1).pack(anchor="w", padx=20)
                    CTkRadioButton(mt_win, text="Gold Member     - 15% Discount", variable=member_type_var, value=2).pack(anchor="w", padx=20)
                    CTkRadioButton(mt_win, text="Silver Member   - 10% Discount", variable=member_type_var, value=3).pack(anchor="w", padx=20)

                    def confirm_member():
                        nonlocal membership_discount_amt, membership_fee, membership_type
                        val = member_type_var.get()
                        if val == 1:
                            membership_discount_amt = total * 0.25
                            membership_fee = 0
                            membership_type = "Platinum Member"
                        elif val == 2:
                            membership_discount_amt = total * 0.15
                            membership_fee = 0
                            membership_type = "Gold Member"
                        elif val == 3:
                            membership_discount_amt = total * 0.10
                            membership_fee = 0
                            membership_type = "Silver Member"
                        else:
                            messagebox.showerror("Error", "Please select a membership type.")
                            return
                        mt_win.destroy()
                        mem_win.destroy()
                        dis_total = total - membership_discount_amt
                        proceed_to_delivery(dis_total)

                    CTkButton(mt_win, text="Confirm", command=confirm_member, fg_color="#601E88", text_color="white").pack(pady=20)

                member_type_win()

            elif val == 2:
                def buy_mem_win():
                    bm_win = CTkToplevel(mem_win)
                    bm_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
                    bm_win.title("Buy Membership")
                    bm_win.geometry(f"400x320+{centre_x}+{centre_y}")
                    bm_win.lift()
                    bm_win.attributes("-topmost", True)
                    bm_win.after(10, lambda: bm_win.attributes("-topmost", False))

                    CTkLabel(bm_win, text="Do you want to buy our membership?", font=("Arial", 14)).pack(pady=10)

                    buy_mem_var = IntVar(value=0)

                    CTkRadioButton(bm_win, text="Yes", variable=buy_mem_var, value=1).pack(anchor="w", padx=20)
                    CTkRadioButton(bm_win, text="No", variable=buy_mem_var, value=2).pack(anchor="w", padx=20)

                    def confirm_buy():
                        nonlocal membership_discount_amt, membership_fee, membership_type
                        val = buy_mem_var.get()
                        if val == 1:
                            def membership_type_buy_win():
                                mtb_win = CTkToplevel(bm_win)
                                mtb_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
                                mtb_win.title("Select Membership Type to Buy")
                                mtb_win.geometry(f"400x280+{centre_x}+{centre_y}")
                                mtb_win.lift()
                                mtb_win.attributes("-topmost", True)
                                mtb_win.after(10, lambda: mtb_win.attributes("-topmost", False))

                                CTkLabel(mtb_win, text="Choose membership to buy", font=("Arial", 14)).pack(pady=10)
                                member_type_var = IntVar(value=0)

                                CTkRadioButton(mtb_win, text="Platinum Member - Rs. 6000 Fee + 25% Discount", variable=member_type_var, value=1).pack(anchor="w", padx=20)
                                CTkRadioButton(mtb_win, text="Gold Member     - Rs. 4500 Fee + 15% Discount", variable=member_type_var, value=2).pack(anchor="w", padx=20)
                                CTkRadioButton(mtb_win, text="Silver Member   - Rs. 3000 Fee + 10% Discount", variable=member_type_var, value=3).pack(anchor="w", padx=20)

                                def confirm_buy_type():
                                    nonlocal membership_discount_amt, membership_fee, membership_type
                                    val = member_type_var.get()
                                    if val == 1:
                                        membership_discount_amt = total * 0.25
                                        membership_fee = 6000
                                        membership_type = "Platinum Member"
                                    elif val == 2:
                                        membership_discount_amt = total * 0.15
                                        membership_fee = 4500
                                        membership_type = "Gold Member"
                                    elif val == 3:
                                        membership_discount_amt = total * 0.10
                                        membership_fee = 3000
                                        membership_type = "Silver Member"
                                    else:
                                        messagebox.showerror("Error", "Please select a membership type.")
                                        return
                                    mtb_win.destroy()
                                    bm_win.destroy()
                                    mem_win.destroy()
                                    dis_total = total - membership_discount_amt
                                    proceed_to_delivery(dis_total)

                                CTkButton(mtb_win, text="Confirm", command=confirm_buy_type, fg_color="#601E88", text_color="white").pack(pady=20)

                            membership_type_buy_win()
                        elif val == 2:
                            membership_discount_amt = 0
                            membership_fee = 0
                            membership_type = "No Membership"
                            bm_win.destroy()
                            mem_win.destroy()
                            proceed_to_delivery(total)
                        else:
                            messagebox.showerror("Error", "Please select an option.")

                    CTkButton(bm_win, text="Confirm", command=confirm_buy, fg_color="#601E88", text_color="white").pack(pady=20)

                buy_mem_win()

            else:
                messagebox.showerror("Error", "Please select if you are a member or not.")

        CTkButton(mem_win, text="Next", command=on_next, fg_color="#601E88", text_color="white").pack(pady=20)

    def ask_gift_wrap():
        gift_win = CTkToplevel(cart_win)
        gift_win.iconbitmap(os.path.join(BASE_DIR, 'myico.ico'))
        gift_win.title("Gift Wrap Option")
        gift_win.geometry(f"400x250+{centre_x}+{centre_y}")
        gift_win.lift()
        gift_win.attributes("-topmost", True)
        gift_win.after(10, lambda: gift_win.attributes("-topmost", False))

        CTkLabel(gift_win, text="Do you want your items gift wrapped?", font=("Arial", 14)).pack(pady=10)

        gift_var = IntVar(value=0)

        CTkRadioButton(gift_win, text="Yes (Rs. 500)", variable=gift_var, value=1).pack(anchor="w", padx=20)
        CTkRadioButton(gift_win, text="No", variable=gift_var, value=2).pack(anchor="w", padx=20)

        def confirm_gift():
            wrap_charge = 0
            if gift_var.get() == 1:
                wrap_charge = 500
            elif gift_var.get() == 2:
                wrap_charge = 0
            else:
                messagebox.showerror("Error", "Please select an option.")
                return
            gift_win.destroy()
            proceed_to_membership(wrap_charge)

        CTkButton(gift_win, text="Confirm", command=confirm_gift, fg_color="#601E88", text_color="white").pack(pady=20)

    def checkout():
        ask_gift_wrap()

    CTkButton(cart_win, text="Checkout", command=checkout, fg_color="#601E88", text_color="white").pack(pady=15)
    CTkButton(cart_win, text="Close", command=cart_win.destroy, fg_color="#cccccc", text_color="#000000").pack()

CTkButton(button_frame, text="Add to Cart", command=add_to_cart, fg_color="#601E88", text_color="white", width=160).pack(side="left", padx=20)
CTkButton(button_frame, text="View Cart", command=show_cart, fg_color="#601E88", text_color="white", width=160).pack(side="right", padx=20)

app.mainloop()