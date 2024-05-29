import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import messagebox
from database.data.models.Note import Note
from notes.view.CreateWindow import CreateWindow
from notes.view.MyComponents.NoteView import NoteView

from database.logic.note_data_logic import NoteDataLogic

from gui.entrance import CreateEntrance
from gui.Registration import CreateRegistration
from database.data import db_functions_person as db

class MainWindow(tk.Tk):
    def __init__(self, connection, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection = connection

        self.button_create = None
        self.listbox = None
        self.search = None
        self.search_button = None
        self.person = None
        self.button_registration = None
        self.button_entrance = None

        self.search_value = tk.StringVar(value="")

        self.title("My Application")
        self.resizable(False, False)
        self.geometry("800x500")

        self.create_widgets()
        self.load()

    def create_widgets(self):
        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        search_container = tk.Frame(contanier)
        search_container.pack(fill=tk.BOTH)

        self.search = tk.Entry(search_container, textvariable=self.search_value)
        self.search.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.search_button = tk.Button(search_container, text="Go")
        self.search_button.pack(side=tk.RIGHT)
        self.search_button['command'] = self.__search
        Hovertip(self.search_button, "Search button")

        self.listbox = tk.Frame(contanier)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        self.button_create = tk.Button(contanier, text="Create")
        self.button_create['command'] = self.__open_create_window
        self.button_create.pack()

        self.button_registration = tk.Button(contanier, text="Регистрация")
        self.button_registration['command'] = self.__open_create_registration
        self.button_registration.pack()

        self.button_entrance = tk.Button(contanier, text="Вход")
        self.button_entrance['command'] = self.__open_create_entrance
        self.button_entrance.pack()


    def clear(self):
        for widget in self.listbox.winfo_children():
            widget.destroy()
    
    def load(self):
        self.clear()

        value = self.search_value.get().strip()

        if value is not None and len(value) > 0:
            notes: list[Note] = NoteDataLogic.get_by_name(self.connection, value)
        else:
            notes: list[Note] = NoteDataLogic.get_all(self.connection)
        x, y = 0, 0

        for note in notes:
            noteview = NoteView(self.listbox, note)
            noteview.set_event(self.__delete_note)
            noteview.place(x=x, y=y)
            x += 150

            if x > 700:
                x = 0
                y += 120

    def __search(self):
        self.load()

    def __delete_note(self, note_id: int):
        result = messagebox.askyesno(title="Удаление", message="Вы точно хотите удалить?")
        if result:
            NoteDataLogic.delete_by_id(self.connection, note_id)
            self.load()

    def __open_create_window(self):
        create_window = CreateWindow(self, self.connection)
        note = create_window.new_note

        NoteDataLogic.insert(self.connection, note)

        self.load()

    def __open_create_registration(self):
        create_window = CreateRegistration(self)
        person = create_window.new_person

        db.insert(self.connection, person)

        self.load()

    def __open_create_entrance(self):
        create_window = CreateEntrance(self, self.connection)
        if create_window.is_login():
            self.person = create_window.login_person
            self.load()