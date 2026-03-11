import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")
app.title("Greeting GUI")

label = ctk.CTkLabel(app, text="Enter your name:")
label.pack(pady=10)

entry = ctk.CTkEntry(app)
entry.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

def button_callback():
    name = entry.get()
    result_label.configure(text=f"Hello {name}!")

    label1 = ctk.CTkLabel(app, text="You are currently using a CustomTkinter GUI")
    label1.pack(pady=5)
    
    label2 = ctk.CTkLabel(app, text="It is in Python 3.13")
    label2.pack(pady=5)

button = ctk.CTkButton(app, text="Greet", command=button_callback)
button.pack(pady=10)

app.mainloop()