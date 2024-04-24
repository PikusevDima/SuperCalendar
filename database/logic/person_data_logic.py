import database.data.db_functions as db
from database.data.models import Person


class PersonDataLogic:
    @staticmethod
    def get_all(connection) -> list[Person]:
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection, person_id: int) -> Person:
        people = PersonDataLogic.get_all(connection)
        for person in people:
            if person.id == person_id:
                return person

        return None

    @staticmethod
    def insert(connection, person: Person) -> bool:
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
    def get_by_login(connection, login: str) -> list[Person]:
        if len(login) == 0:
            return []

        people = db.get_all(connection)

        if model[:3] == 'id:':
            return list(
                filter(
                    lambda x: int(model[3]) == x.id,
                    cars
                )
            )

        return list(
            filter(
                lambda x: model.lower() in x.model.lower(),
                cars
            )
        )
