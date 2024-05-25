import tkinter as tk
from database.data.models.Note import Note


class NoteView(tk.Frame):
    def __init__(self, parent, note: Note):
        # self.__background = "blue"

        super().__init__(parent,
                         borderwidth=1,
                         highlightthickness=1,
                         highlightbackground="red",
                         padx=10,
                         pady=10)

        self.__note = note

        self.__on_delete = None

        self.label_name = None
        self.label_text = None
        self.label_person_id = None
        self.button = None

        self.create_widgets()

    def set_event(self, event):
        self.__on_delete = event

    def create_widgets(self):
        self.label_name = tk.Label(self, text="name: " + self.__note.name)
        self.label_name.pack(fill=tk.BOTH, expand=True)
        self.label_text = tk.Label(self, text=str(self.__note.text))
        self.label_text.pack()
        self.label_person_id = tk.Label(self, text=str(self.__note.person_id))
        self.label_person_id.pack()

        self.button = tk.Button(self, text="Delete")
        self.button['command'] = self.__delete
        self.button.pack()

    def __delete(self):
        self.__on_delete(self.__note.id)
