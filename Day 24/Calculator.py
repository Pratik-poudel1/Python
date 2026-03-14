import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Calculator")
app.geometry("600x300")

expression = ""

display = ctk.CTkEntry(app, width=560, height=40)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def press(num):
    global expression
    expression = expression + str(num)
    display.delete(0, "end")
    display.insert(0, expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""


def clear():
    global expression
    expression = ""
    display.delete(0, "end")


# Row 1
b1 = ctk.CTkButton(app, text="7", command=lambda: press(7))
b1.grid(row=1, column=0, padx=5, pady=5)

b2 = ctk.CTkButton(app, text="8", command=lambda: press(8))
b2.grid(row=1, column=1, padx=5, pady=5)

b3 = ctk.CTkButton(app, text="9", command=lambda: press(9))
b3.grid(row=1, column=2, padx=5, pady=5)

b4 = ctk.CTkButton(app, text="/", command=lambda: press("/"))
b4.grid(row=1, column=3, padx=5, pady=5)


# Row 2
b5 = ctk.CTkButton(app, text="4", command=lambda: press(4))
b5.grid(row=2, column=0, padx=5, pady=5)

b6 = ctk.CTkButton(app, text="5", command=lambda: press(5))
b6.grid(row=2, column=1, padx=5, pady=5)

b7 = ctk.CTkButton(app, text="6", command=lambda: press(6))
b7.grid(row=2, column=2, padx=5, pady=5)

b8 = ctk.CTkButton(app, text="*", command=lambda: press("*"))
b8.grid(row=2, column=3, padx=5, pady=5)


# Row 3
b9 = ctk.CTkButton(app, text="1", command=lambda: press(1))
b9.grid(row=3, column=0, padx=5, pady=5)

b10 = ctk.CTkButton(app, text="2", command=lambda: press(2))
b10.grid(row=3, column=1, padx=5, pady=5)

b11 = ctk.CTkButton(app, text="3", command=lambda: press(3))
b11.grid(row=3, column=2, padx=5, pady=5)

b12 = ctk.CTkButton(app, text="-", command=lambda: press("-"))
b12.grid(row=3, column=3, padx=5, pady=5)


# Row 4
b13 = ctk.CTkButton(app, text="0", command=lambda: press(0))
b13.grid(row=4, column=0, padx=5, pady=5)

b14 = ctk.CTkButton(app, text=".", command=lambda: press("."))
b14.grid(row=4, column=1, padx=5, pady=5)

b15 = ctk.CTkButton(app, text="=", command=equal)
b15.grid(row=4, column=2, padx=5, pady=5)

b16 = ctk.CTkButton(app, text="+", command=lambda: press("+"))
b16.grid(row=4, column=3, padx=5, pady=5)


# Clear button
clear_button = ctk.CTkButton(app, text="Clear", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, pady=10)

app.mainloop()