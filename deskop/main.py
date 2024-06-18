import customtkinter


def open_main_window():
    customtkinter.set_appearance_mode( "dark" )
    customtkinter.set_default_color_theme( "dark-blue" )

    root = customtkinter.CTk()
    window_width = 500
    window_height = 350

    # Get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Find the center point
    center_x = int( screen_width / 2 - window_width / 2 )
    center_y = int( screen_height / 2 - window_height / 2 )

    # Set the position of the window to the center of the screen
    root.geometry( f'{window_width}x{window_height}+{center_x}+{center_y}' )

    frame = customtkinter.CTkFrame( master=root )
    frame.pack( pady=20, padx=60, fill="both", expand=True )

    label = customtkinter.CTkLabel( master=frame, text="Main Application", font=("Roboto", 24) )
    label.pack( pady=12, padx=10 )

    button = customtkinter.CTkButton( master=frame, text="Button", command=lambda: print( "Button Clicked" ) )
    button.pack( pady=12, padx=10 )

    root.mainloop()


if __name__ == "__main__":
    open_main_window()
