# desktop/LoginView/login_script.py

from customtkinter import *
from tkinter import messagebox
import requests
import sys
import os

# Aplic directoriul unde se afla fileul main
sys.path.append( os.path.dirname( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) ) )
import main

# URL API
BASE_URL = "http://127.0.0.1:8000"


class LoginApp( CTk ):
    def __init__(self):
        super().__init__()

        self.title( "Coffee LeCoupage" )
        self.geometry( "500x400" )

        set_appearance_mode( "dark" )
        set_default_color_theme( "dark-blue" )

        self.current_frame = None
        self.switch_frame( LoginFrame )

    def switch_frame(self, frame_class):
        new_frame = frame_class( self )
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack( pady=20, padx=60, fill="both", expand=True )


class LoginFrame( CTkFrame ):
    def __init__(self, master):
        super().__init__( master )

        title_label = CTkLabel( master=self, text="Login", font=("Roboto", 24) )
        title_label.pack( pady=12, padx=10 )

        self.entry_username = CTkEntry( master=self, placeholder_text="Username" )
        self.entry_username.pack( pady=12, padx=10 )

        self.entry_password = CTkEntry( master=self, placeholder_text="Password", show="*" )
        self.entry_password.pack( pady=12, padx=10 )

        login_button = CTkButton( master=self, text="Login", command=self.login_user )
        login_button.pack( pady=12, padx=10 )

        switch_button = CTkButton( master=self, text="Register", command=lambda: master.switch_frame( RegisterFrame ) )
        switch_button.pack( pady=12, padx=10 )

    def login_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post( f"{BASE_URL}/login/", json=data )
            response.raise_for_status()
            response_json = response.json()
            if response.status_code == 200:
                messagebox.showinfo( "Success", "Login successful" )
                self.master.destroy()  # Inchide viewul de Login
                main.start_main_application()  # Deschide View de Main
            else:
                messagebox.showerror( "Error", response_json.get( "detail" ) )
        except requests.exceptions.HTTPError as http_err:
            print( f"HTTP error occurred: {http_err}" )
            messagebox.showerror( "Error", f"HTTP error occurred: {http_err}" )
        except Exception as err:
            print( f"Other error occurred: {err}" )
            messagebox.showerror( "Error", f"An error occurred: {err}" )


class RegisterFrame( CTkFrame ):
    def __init__(self, master):
        super().__init__( master )

        title_label = CTkLabel( master=self, text="Register", font=("Roboto", 24) )
        title_label.pack( pady=12, padx=10 )

        self.entry_username = CTkEntry( master=self, placeholder_text="Username" )
        self.entry_username.pack( pady=12, padx=10 )

        self.entry_password = CTkEntry( master=self, placeholder_text="Password", show="*" )
        self.entry_password.pack( pady=12, padx=10 )

        self.entry_confirm_password = CTkEntry( master=self, placeholder_text="Confirm Password", show="*" )
        self.entry_confirm_password.pack( pady=12, padx=10 )

        self.is_active_var = IntVar( value=1 )  # 1 for True, 0 for False
        self.check_is_active = CTkCheckBox( master=self, text="Is Active", variable=self.is_active_var )
        self.check_is_active.pack( pady=12, padx=10 )

        register_button = CTkButton( master=self, text="Register", command=self.register_user )
        register_button.pack( pady=12, padx=10 )

        switch_button = CTkButton( master=self, text="Login", command=lambda: master.switch_frame( LoginFrame ) )
        switch_button.pack( pady=12, padx=10 )

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        is_active = bool( self.is_active_var.get() )

        if password != confirm_password:
            messagebox.showerror( "Error", "Passwords do not match" )
            return

        data = {
            "username": username,
            "password": password,
            "is_active": is_active
        }
        try:
            response = requests.post( f"{BASE_URL}/login/", json=data )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print( f"HTTP error occurred: {http_err}" )
            messagebox.showerror( "Error", f"HTTP error occurred: {http_err}" )
        except Exception as err:
            print( f"Other error occurred: {err}" )
            messagebox.showerror( "Error", f"An error occurred: {err}" )
        return None


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
