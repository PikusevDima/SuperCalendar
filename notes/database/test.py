from database.logic.note_data_logic import noteDataLogic
import sqlite3
import pprint

connection = sqlite3.connect('../../database_all.db')

pprint.pprint(noteDataLogic.get_all(connection))
pprint.pprint(noteDataLogic.get_by_id(connection, 7))
pprint.pprint(noteDataLogic.get_by_name(connection, "Audi"))

connection.close()
