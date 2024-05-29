import sqlite3
from database.data import sql_scripts
from database.data.notes.Note import Note


def get_all(connection: sqlite3.Connection) -> list[Note]:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.note_sql_script_select_all)
        value: list[tuple] = cursor.fetchall()
        notes: list[Note] = []

        for data in value:
            note = Note.of(data)
            notes.append(note)

        return notes
    except Exception as e:
        print(e)
        return []


def insert(connection: sqlite3.Connection, note: Note) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.note_sql_script_insert, note.to_data())
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_all(connection: sqlite3.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.note_sql_script_delete_all)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_by_id(connection: sqlite3.Connection, note_id: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.note_sql_script_delete_by_id, (note_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
