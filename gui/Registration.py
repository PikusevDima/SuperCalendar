import tkinter as tk
from database.data.models.Person import Person
from tkinter import messagebox


class CreateRegistration(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.submit_button = None
        self.new_person = None

        self.title("Calendar")
        self.geometry("400x300")

        self.__login = tk.StringVar()
        self.__password = tk.StringVar()
        self.__password2 = tk.StringVar()

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

        # password2
        contanier_password2 = tk.Frame(contanier)
        contanier_password2.pack(fill=tk.BOTH)

        label_password2 = tk.Label(contanier_password2, text="Repeat your password")
        label_password2.pack(side=tk.LEFT)

        entry_password2 = tk.Entry(contanier_password2, textvariable=self.__password2)
        entry_password2.pack(side=tk.RIGHT, fill=tk.X)
        # password end2

        self.submit_button = tk.Button(contanier, text="Submit")
        self.submit_button['command'] = self.submit
        self.submit_button.pack(fill=tk.BOTH)

            

    def submit(self):
        if self.__password2.get() == self.__password.get():
            if len(self.__password.get()) > 3:
                self.new_person = Person(
                    None,
                    self.__login.get(),
                    self.__password2.get()
                )
                self.close()
            else:
                messagebox.showerror("Ошибка", "Пароль должен быть больше 3 символов")
        else:
            messagebox.showerror("Ошибка", "Пароли не совпадают.")


    def close(self):
        self.destroy()

    def load(self):
        ...
