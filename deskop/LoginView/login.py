import tkinter
import customtkinter
import sys
import os

# Add the parent directory to the sys.path to import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Le Coupage")
window_width = 500
window_height = 350

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def login():
    root.destroy()  # Close the login window
    main.open_dashboard()  # Call the function from main.py to open the main window


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

labelWelcome = customtkinter.CTkLabel(master=frame, text="Bine ati venit la Coupage", font=("Roboto", 24))
labelWelcome.pack(pady=12, padx=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = customtkinter.CTkEntry(master=frame, placeholder_text="Parola", show="*")
password.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

root.mainloop()
