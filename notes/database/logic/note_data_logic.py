import database.data.db_functions as db
from database.data.notes import Note


class NoteDataLogic:
    @staticmethod
    def get_all(connection) -> list[Note]:
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection, note_id: int) -> Note:
        notes = NoteDataLogic.get_all(connection)
        for note in notes:
            if note.id == note_id:
                return note

        return None

    @staticmethod
    def insert(connection, note: Note) -> bool:
        if note.person_id < 0:
            return False

        if note is None:
            return False
        return db.insert(connection, note)

    @staticmethod
    def delete_all(connection) -> bool:
        return db.delete_all(connection)

    @staticmethod
    def delete_by_id(connection, note_id: int):
        if note_id < 0:
            return False
        return db.delete_by_id(connection, note_id)

    @staticmethod
    def get_by_name(connection, name: str) -> list[Note]:
        if len(name) == 0:
            return []

        notes = db.get_all(connection)

        if name[:3] == 'id:':
            return list(
                filter(
                    lambda x: int(name[3]) == x.id,
                    notes
                )
            )

        return list(
            filter(
                lambda x: name.lower() in x.name.lower(),
                notes
            )
        )
