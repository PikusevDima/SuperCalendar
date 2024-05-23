import tkinter as tk
from database.data.notes.Note import Note


class CreateWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.submit_button = None
        self.new_note = None

        self.title("My Application")
        self.geometry("300x150")

        self.__name = tk.StringVar()
        self.__text = tk.StringVar()
        self.__person_id = tk.StringVar(value="0")

        self.create_widgets()
        self.load()

        self.grab_set()
        self.wait_window()

    def create_widgets(self):
        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)
        # name
        contanier_name = tk.Frame(contanier)
        contanier_name.pack(fill=tk.BOTH)

        label_name = tk.Label(contanier_name, text="name")
        label_name.pack(side=tk.LEFT)

        entry_name = tk.Entry(contanier_name, textvariable=self.__name)
        entry_name.pack(side=tk.RIGHT, fill=tk.X)
        # name end

        # text
        contanier_text = tk.Frame(contanier)
        contanier_text.pack(fill=tk.BOTH)

        label_text = tk.Label(contanier_text, text="text")
        label_text.pack(side=tk.LEFT)

        entry_text = tk.Entry(contanier_text, textvariable=self.__text)
        entry_text.pack(side=tk.RIGHT, fill=tk.X)
        # text end

        # person_id
        contanier_person_id = tk.Frame(contanier)
        contanier_person_id.pack(fill=tk.BOTH)

        label_person_id = tk.Label(contanier_person_id, text="person_id")
        label_person_id.pack(side=tk.LEFT)

        entry_person_id = tk.Entry(contanier_person_id, textvariable=self.__person_id)
        entry_person_id.pack(side=tk.RIGHT, fill=tk.X)
        # person_id

        self.submit_button = tk.Button(contanier, text="Submit")
        self.submit_button['command'] = self.submit
        self.submit_button.pack(fill=tk.BOTH)

    def submit(self):
        if len(self.__name.get()) == 0:
            return

        try:
            self.new_note = Note(
                None,
                self.__name.get(),
                self.__text.get(),
                int(self.__person_id.get())
            )
            self.close()
        except Exception as e:
            print(e)

    def close(self):
        self.destroy()

    def load(self):
        ...
