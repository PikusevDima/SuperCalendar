from gui.MainWindow import MainWindow as Wn
import sqlite3

connection = sqlite3.connect('database.db')
cursos = connection.cursor()
#
# cursos.execute(sql_scripts.person_sql_script_create_table)
#
# cursos.execute(sql_scripts.person_sql_script_insert, ("Vasya", "hg5"))

if __name__ == '__main__':
    window = Wn(connection=connection)
    window.mainloop()

connection.close()
