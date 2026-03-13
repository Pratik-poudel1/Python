import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("Unit Converter")
width = 300
height = 300
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x}+{y}")

# Variables
value_var = ctk.StringVar()
unit_var = ctk.StringVar(value="km -> miles")

# Conversion function
def convert(*args):
    try:
        value = float(value_var.get())
        unit = unit_var.get()
        if unit == "km -> miles":
            result = value * 0.621371
        elif unit == "miles -> km":
            result = value * 1.60934
        elif unit == "kg -> lbs":
            result = value * 2.20462
        elif unit == "lbs -> kg":
            result = value * 0.453592
        elif unit == "C -> F":
            result = (value * 9/5) + 32
        elif unit == "F -> C":
            result = (value - 32) * 5/9
        result_label.configure(text=f"Result: {result:.2f}")

    except:
        result_label.configure(text="Enter a valid number")

# Trace changes
value_var.trace_add("write", convert)
unit_var.trace_add("write", convert)

# Entry
entry = ctk.CTkEntry(app, textvariable=value_var, placeholder_text="Enter value")
entry.pack(pady=20)

# Dropdown
units = [
    "km -> miles",
    "miles -> km",
    "kg -> lbs",
    "lbs -> kg",
    "C -> F",
    "F -> C"
]

menu = ctk.CTkOptionMenu(app, values=units, variable=unit_var)
menu.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(app, text="Result:")
result_label.pack(pady=20)

# Run
app.mainloop()