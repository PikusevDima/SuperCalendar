import tkinter as tk
from database.data.models.person import Person


class PersonView(tk.Frame):
    def __init__(self, parent, person: Person):
        # self.__background = "blue"

        super().__init__(parent,
                         borderwidth=1,
                         highlightthickness=1,
                         highlightbackground="red",
                         padx=10,
                         pady=10)

        self.__person = person

        self.__on_delete = None

        self.label_login = None
        self.label_password = None
        self.button = None

        self.create_widgets()

    def set_event(self, event):
        self.__on_delete = event

    def create_widgets(self):
        self.label_login = tk.Label(self, text="Login: " + self.__person.login)
        self.label_login.pack(fill=tk.BOTH, expand=True)
        self.label_password = tk.Label(self, text=str(self.__person.password))
        self.label_password.pack()

        self.button = tk.Button(self, text="Delete")
        self.button['command'] = self.__delete
        self.button.pack()

    def __delete(self):
        self.__on_delete(self.__person.id)
