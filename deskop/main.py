import customtkinter


def open_dashboard():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.title("Le Coupage")
    window_width = 1280
    window_height = 920

    # Get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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

    frameHome = customtkinter.CTkFrame(master=content_frame)
    frameSettings = customtkinter.CTkFrame(master=content_frame)

    for frame in (frameHome, frameSettings):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    labelhello = customtkinter.CTkLabel(master=frameHome, text="Dashboard Home", font=("Roboto", 24))
    labelhello.pack(pady=20, padx=20)

    label2 = customtkinter.CTkLabel(master=frameSettings, text="hey", font=("Roboto", 24))
    label2.pack(pady=20, padx=20)

    home = customtkinter.CTkButton(master=sidebar_frame, text="Home", command=lambda: change_frame(frameHome))
    home.pack(pady=10, padx=10)

    settings = customtkinter.CTkButton(master=sidebar_frame, text="Settings", command=lambda: change_frame(frameSettings))
    settings.pack(pady=10, padx=10)

    orders = customtkinter.CTkButton(master=sidebar_frame, text="Orders", command=lambda: change_frame(frameSettings))
    orders.pack(pady=10, padx=10)

    # close_button = customtkinter.CTkButton(master=main_frame, text="X", command=close_application, fg_color="red", hover_color="dark red")
    # close_button.place(relx=1.0, rely=0.0, anchor="ne")

    change_frame(frameHome)

    root.mainloop()


if __name__ == "__main__":
    open_dashboard()
