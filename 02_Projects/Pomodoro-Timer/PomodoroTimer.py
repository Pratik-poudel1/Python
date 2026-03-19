import customtkinter as ctk
import winsound

# appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# window
app = ctk.CTk()
app.title("Pomodoro Timer")
app.geometry("300x250")

# time (25 minutes)
time_left = 25 * 60
running = False

# timer label
timer_label = ctk.CTkLabel(app, text="25:00", font=("Arial", 40))
timer_label.pack(pady=20)

# progress bar
progress = ctk.CTkProgressBar(app, width=250)
progress.pack(pady=10)
progress.set(0)

# update timer
def update_timer():
    global time_left, running
    
    if running and time_left > 0:
        time_left -= 1
        
        minutes = time_left // 60
        seconds = time_left % 60
        
        timer_label.configure(text=f"{minutes:02}:{seconds:02}")
        
        progress.set((1500 - time_left) / 1500)
        
        app.after(1000, update_timer)
        
    elif time_left == 0:
        winsound.Beep(1000, 500)
        running = False

# start button
def start_timer():
    global running
    if not running:
        running = True
        update_timer()

# reset button
def reset_timer():
    global time_left, running
    running = False
    time_left = 25 * 60
    timer_label.configure(text="25:00")
    progress.set(0)

# buttons
start_btn = ctk.CTkButton(app, text="Start", command=start_timer)
start_btn.pack(pady=5)

reset_btn = ctk.CTkButton(app, text="Reset", command=reset_timer)
reset_btn.pack(pady=5)

app.mainloop()