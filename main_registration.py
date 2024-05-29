from gui.MainWindow import MainWindow as Wn
import sqlite3
from database.data.sql_scripts import *
# from notes.database.data.sql_scripts import *

connection = sqlite3.connect('../database_all.db')
cursos = connection.cursor()
#
cursos.execute(person_sql_script_create_table)
#
# cursos.execute(note_sql_script_create_table)

if __name__ == '__main__':
    window = Wn(connection=connection)
    window.mainloop()

connection.close()
