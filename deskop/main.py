# desktop/main.py
from customtkinter import *


class MainApp( CTk ):
    def __init__(self):
        super().__init__()

        self.title( "Main Application" )
        self.geometry( "500x400" )

        set_appearance_mode( "dark" )
        set_default_color_theme( "dark-blue" )

        self.create_widgets()

    def create_widgets(self):
        title_label = CTkLabel( master=self, text="Main Application", font=("Roboto", 24) )
        title_label.pack( pady=12, padx=10 )


def start_main_application():
    app = MainApp()
    app.mainloop()
