import tkinter as tk
from database.data.models.person import Person
from database.data import db_functions as db
from gui.CreateWindow import CreateWindow
from gui.Registration import CreateRegistration


class MainWindow(tk.Tk):
    def __init__(self, connection, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = connection

        self.button_create = None
        self.button_registration = None
        self.listbox = None

        self.title("My Application")
        self.geometry("800x500")

        self.create_widgets()
        self.load()

    def create_widgets(self):
        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)

        self.listbox = tk.Listbox(contanier, selectmode=tk.SINGLE)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        self.button_create = tk.Button(contanier, text="Create")
        self.button_create['command'] = self.__open_create_window
        self.button_create.pack()

        self.button_registration = tk.Button(contanier, text="Registration")
        self.button_registration['command'] = self.__open_create_registration()
        self.button_registration.pack()

    def load(self):
        self.listbox.delete('0', 'end')

        people: list[Person] = db.select(self.connection)

        for person in self.__convert_to_str(people, ["id", "login", "password"]):
            self.listbox.insert(tk.END, person)

    def __open_create_window(self):
        create_window = CreateWindow(self)
        person = create_window.new_person

        db.insert(self.connection, person)

        self.load()

    def __pattern(self, values: list[str]) -> str:
        if len(values) == 3:
            return f"| {values[0]:^5} | {values[1]:^70} | {values[2]:^15}"
        return ""

    def __convert_to_str(self, person_list: list[Person], titles: list[str]) -> list[str]:
        output = []
        for person in person_list:
            value = self.__pattern(person.get())
            output.append(value)
        return output
