import os
import time
import getpass
from datetime import datetime
import tkinter as tk

# Config
file_name = "iamsafe.txt"
parent_dir = "C:/Users/TheAstronautGuy/Desktop"
file_path = os.path.join(parent_dir, file_name)
log_path = os.path.join(parent_dir, "guardian_logs.txt")


# Hide the log file
def hide_log_file():
    os.system(f'attrib +h "{log_path}"')


# GUI Warning Function (Transparent background)
def show_warning(message, duration=1000):
    root = tk.Tk()
    root.attributes('-topmost', True)  # Always on top
    root.overrideredirect(True)  # No border/window
    root.configure(bg='black')  # Set black background for root window
    root.wm_attributes("-transparentcolor", "black")  # Make black transparent

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Label with transparent background and only text
    label = tk.Label(root, text=message, font=('Courier', 36, 'bold'), fg='red', bg='black')
    label.place(relx=0.5, rely=0.5, anchor='center')

    root.after(duration, root.destroy)
    root.mainloop()


# Force Shutdown Function
def force_shutdown():
    os.system("shutdown /f /t 0")  # Force shutdown immediately, no prompt to cancel


# Delay before checking
time.sleep(5)

# Check for iamsafe.txt
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    # Log the intrusion
    user = getpass.getuser()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as log_file:
        log_file.write(f"[{now}] Unauthorized access by {user}. Shutdown initiated.\n")

    # Hide the log file
    hide_log_file()

    # Display countdown
    for i in range(10, 0, -1):
        show_warning(f"🚨 UNAUTHORIZED ACCESS\nSystem will shutdown in {i} seconds...", duration=1000)

    # Force shutdown after the countdown
    force_shutdown()