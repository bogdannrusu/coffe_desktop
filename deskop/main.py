import tkinter
import customtkinter


def open_dashboard():
    customtkinter.set_appearance_mode( "dark" )
    customtkinter.set_default_color_theme( "dark-blue" )

    root = customtkinter.CTk()

    # Set the window to full screen
    root.attributes( '-fullscreen', True )

    def change_frame(new_frame):
        new_frame.tkraise()

    def exit_fullscreen(event=None):
        root.attributes( '-fullscreen', False )

    root.bind( "<Escape>", exit_fullscreen )  # Bind the Escape key to exit full-screen

    # Main frame
    main_frame = customtkinter.CTkFrame( master=root )
    main_frame.pack( fill="both", expand=True )

    # Sidebar
    sidebar_frame = customtkinter.CTkFrame( master=main_frame, width=200 )
    sidebar_frame.pack( side="left", fill="y" )

    # Main content area
    content_frame = customtkinter.CTkFrame( master=main_frame )
    content_frame.pack( side="right", fill="both", expand=True )

    frame1 = customtkinter.CTkFrame( master=content_frame )
    frame2 = customtkinter.CTkFrame( master=content_frame )

    for frame in (frame1, frame2):
        frame.place( x=0, y=0, relwidth=1, relheight=1 )

    label1 = customtkinter.CTkLabel( master=frame1, text="Dashboard Home", font=("Roboto", 24) )
    label1.pack( pady=20, padx=20 )

    label2 = customtkinter.CTkLabel( master=frame2, text="Settings", font=("Roboto", 24) )
    label2.pack( pady=20, padx=20 )

    button1 = customtkinter.CTkButton( master=sidebar_frame, text="Home", command=lambda: change_frame( frame1 ) )
    button1.pack( pady=10, padx=10 )

    button2 = customtkinter.CTkButton( master=sidebar_frame, text="Settings", command=lambda: change_frame( frame2 ) )
    button2.pack( pady=10, padx=10 )

    change_frame( frame1 )  # Show the home frame by default

    root.mainloop()


if __name__ == "__main__":
    open_dashboard()
