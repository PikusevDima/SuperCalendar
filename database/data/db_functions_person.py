import sqlite3
from database.data import sql_scripts
from database.data.models.Person import Person


def select(connection: sqlite3.Connection) -> list[{Person}]:
    cursor = connection.cursor()
    cursor.execute(sql_scripts.person_sql_script_select_all)
    value: list[tuple] = cursor.fetchall()
    people: list[Person] = []

    for data in value:
        person = Person.of(data)
        people.append(person)

    return people


def insert(connection: sqlite3.Connection, person: Person) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.person_sql_script_insert, person.to_data())
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_all(connection: sqlite3.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.person_sql_script_insert)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_by_id(connection: sqlite3.Connection, person_id: int) -> Person | None:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.person_sql_script_insert, (person_id,))
        value: list[tuple] = cursor.fetchall()
        return Person.of(value[0])
    except Exception as e:
        print(e)
        return None

def get_all(connection: sqlite3.Connection) -> list[Person]:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.person_sql_script_select_all)
        value: list[tuple] = cursor.fetchall()
        people: list[Person] = []

        for data in value:
            person = Person.of(data)
            people.append(person)

        return people
    except Exception as e:
        print(e)
        return []

def get_by_login(connection: sqlite3.Connection, person_login: str) -> Person | None:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.person_sql_script_insert, (person_login,))
        value: list[tuple] = cursor.fetchall()
        return Person.of(value[0])
    except Exception as e:
        print(e)
        return None
