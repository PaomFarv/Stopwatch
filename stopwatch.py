import tkinter as tk
import time

root = tk.Tk()
root.title("StopWatch")
root.config(bg="Black")
root.geometry("600x300")
root.iconbitmap("favicon.ico")

time_label = tk.Label(root,text = "00:00:00",font=("Impact",90),bg="Black",fg="White")
time_label.pack(padx = 10,pady=10)

button_style = {
    "font": ("Helvetica", 20, "bold"),
    "bg": "#4CAF50",  # Green background
    "fg": "white",  # White text
    "relief": "raised",  # Raised effect for 3D appearance
    "bd": 5,  # Border width
    "width": 3,  # Width of the button
    "height": 1,  # Height of the button
    "pady": 10,  # Vertical padding
    "padx": 20,  # Horizontal padding
    "cursor": "hand2"  # Change cursor to hand on hover
}
button_frame = tk.Frame(root,bg="Black")
button_frame.pack(expand=True)

start_time = 0
is_running = False
elapsed_time = 0

def update_time():
    if is_running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        hours = int(elapsed_time) // 3600
        minutes = (int(elapsed_time) % 3600) // 60
        seconds = int(elapsed_time) % 60
        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        time_label.after(1000,update_time)

def start():
    global start_time,is_running
    if not is_running:
        start_time = time.time() - elapsed_time
        is_running = True
        update_time()

def stop():
    global is_running
    is_running = False

def reset():
    global elapsed_time,start_time
    elapsed_time = 0
    start_time = time.time() - elapsed_time
    time_label.config(text="00:00:00")

start_button = tk.Button(button_frame, text="Start", **button_style, command = start)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(button_frame, text="Stop", **button_style, command = stop)
stop_button.pack(side="left", padx=10)

reset_button = tk.Button(button_frame, text="Reset", **button_style, command = reset)
reset_button.pack(side="left", padx=10)


root.mainloop()