import tkinter as tk
from database.data.models.person import Person
import database.data.db_functions as db
import sqlite3

class CreateEntrance(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.submit_button = None
        self.new_person = None

        self.title("My Application")
        self.geometry("300x150")

        self.__login = tk.StringVar()
        self.__password = tk.StringVar()

        self.create_widgets()
        self.load()

        self.grab_set()
        self.wait_window()

    def create_widgets(self):
        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)
        # login
        contanier_login = tk.Frame(contanier)
        contanier_login.pack(fill=tk.BOTH)

        label_login = tk.Label(contanier_login, text="Login")
        label_login.pack(side=tk.LEFT)

        entry_login = tk.Entry(contanier_login, textvariable=self.__login)
        entry_login.pack(side=tk.RIGHT, fill=tk.X)
        # login end

        # password
        contanier_password = tk.Frame(contanier)
        contanier_password.pack(fill=tk.BOTH)

        label_password = tk.Label(contanier_password, text="Password")
        label_password.pack(side=tk.LEFT)

        entry_password = tk.Entry(contanier_password, textvariable=self.__password)
        entry_password.pack(side=tk.RIGHT, fill=tk.X)
        # password end

        self.submit_button = tk.Button(contanier, text="Submit")
        self.submit_button['command'] = self.submit
        self.submit_button.pack(fill=tk.BOTH)

    def submit(self):
        logins = db.get_all()
        for i in logins:
            if self.__login.get() == i:



        self.close()

    def close(self):
        self.destroy()

    def load(self):
        ...
