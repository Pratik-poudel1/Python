import customtkinter as ctk

app = ctk.CTk()
app = ctk.CTk()

width = 400
height = 450
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x}+{y}")
app.title("To-Do List App")

ctk.CTkLabel(app, text="To-Do List", font=("Arial", 24)).pack(pady=10)
entry = ctk.CTkEntry(app, placeholder_text="Enter task")
entry.pack(pady=10)

# scrollable area
task_frame = ctk.CTkScrollableFrame(app, width=350, height=250)
task_frame.pack(pady=10)

def add_task():
    task = entry.get()
    if task == "":
        return

    row = ctk.CTkFrame(task_frame)
    row.pack(fill="x", pady=5, padx=5)

    checkbox = ctk.CTkCheckBox(row, text=task)
    checkbox.pack(side="left", padx=10)

    delete_btn = ctk.CTkButton(row, text="Delete", width=60,command=row.destroy)
    delete_btn.pack(side="right", padx=10)

    entry.delete(0, "end")

# add task button
add_button = ctk.CTkButton(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

app.mainloop()