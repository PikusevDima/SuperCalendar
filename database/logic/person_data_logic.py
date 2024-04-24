import database.data.db_functions as db
from database.data.models import person


class PersonDataLogic:
    @staticmethod
    def get_all(connection) -> list[person]:
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection, person_id: int) -> person:
        people = PersonDataLogic.get_all(connection)
        for person in people:
            if person.id == person_id:
                return person

        return None

    @staticmethod
    def insert(connection, person: person) -> bool:
        if person is None:
            return False
        return db.insert(connection, person)

    @staticmethod
    def delete_all(connection) -> bool:
        return db.delete_all(connection)

    @staticmethod
    def delete_by_id(connection, person_id: int):
        if person_id < 0:
            return False
        return db.delete_by_id(connection, person_id)

    @staticmethod
    def get_by_login(connection, login: str) -> list[person]:
        if len(login) == 0:
            return []

        people = db.get_all(connection)

        if password[:3] == 'id:':
            return list(
                filter(
                    lambda x: int(password[3]) == x.id,
                    people
                )
            )

        return list(
            filter(
                lambda x: people.lower() in x.model.lower(),
                people
            )
        )
