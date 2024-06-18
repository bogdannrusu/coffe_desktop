import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
import customtkinter


def fetch_data():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="your_host",  # Change to your database host
            user="your_username",  # Change to your database username
            password="your_password",  # Change to your database password
            database="your_database"  # Change to your database name
        )

        if conn.is_connected():
            cursor = conn.cursor()
            # Execute a query
            cursor.execute("SELECT * FROM orders")  # Adjust the query to your table and columns

            # Fetch all rows
            rows = cursor.fetchall()

            # Close the connection
            conn.close()

            return rows
        else:
            print("Failed to connect to the database")
            return []

    except Error as e:
        print(f"Error: {e}")
        return []


def open_dashboard():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()

    # Set the window to full screen
    root.attributes('-fullscreen', True)

    def change_frame(new_frame):
        new_frame.tkraise()

    def exit_fullscreen(event=None):
        root.attributes('-fullscreen', False)

    def close_application():
        root.destroy()

    root.bind("<Escape>", exit_fullscreen)  # Bind the Escape key to exit full-screen

    # Main frame
    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(fill="both", expand=True)

    # Sidebar
    sidebar_frame = customtkinter.CTkFrame(master=main_frame, width=200)
    sidebar_frame.pack(side="left", fill="y")

    # Main content area
    content_frame = customtkinter.CTkFrame(master=main_frame)
    content_frame.pack(side="right", fill="both", expand=True)

    frame1 = customtkinter.CTkFrame(master=content_frame)
    frame2 = customtkinter.CTkFrame(master=content_frame)

    for frame in (frame1, frame2):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    label1 = customtkinter.CTkLabel(master=frame1, text="Dashboard Home", font=("Roboto", 24))
    label1.pack(pady=20, padx=20)

    label2 = customtkinter.CTkLabel(master=frame2, text="Settings", font=("Roboto", 24))
    label2.pack(pady=20, padx=20)

    button1 = customtkinter.CTkButton(master=sidebar_frame, text="Home", command=lambda: change_frame(frame1))
    button1.pack(pady=10, padx=10)

    button2 = customtkinter.CTkButton(master=sidebar_frame, text="Settings", command=lambda: change_frame(frame2))
    button2.pack(pady=10, padx=10)

    # Add the red button at the top-right corner
    close_button = customtkinter.CTkButton(master=main_frame, text="X", command=close_application, fg_color="red",
                                           hover_color="dark red")
    close_button.place(relx=1.0, rely=0.0, anchor="ne")

    # Create a new frame for the data grid
    data_frame = customtkinter.CTkFrame(master=content_frame)
    data_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Fetch data from the database
    data = fetch_data()

    # Create the treeview
    columns = ("OrderID", "CustomerName", "OrderDate")  # Adjust these columns according to your table
    tree = ttk.Treeview(data_frame, columns=columns, show='headings')

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Insert data into the treeview
    for row in data:
        tree.insert("", tk.END, values=row)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(data_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(fill="both", expand=True)

    # Add a button in the sidebar to show the data grid
    button3 = customtkinter.CTkButton(master=sidebar_frame, text="Orders", command=lambda: change_frame(data_frame))
    button3.pack(pady=10, padx=10)

    change_frame(frame1)

    root.mainloop()


if __name__ == "__main__":
    open_dashboard()
