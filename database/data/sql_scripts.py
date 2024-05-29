import sqlite3
person_sql_script_create_table = """
    CREATE TABLE IF NOT EXISTS Person (
        id INTEGER PRIMARY KEY,
        login TEXT NOT NULL,
        password TEXT NOT NULL
    )
"""

person_sql_script_insert = """
    INSERT INTO Person (login, password) VALUES (?, ?)
"""

person_sql_script_select_all = """
    SELECT * FROM Person
"""

person_script_select_by_id = """
    SELECT * FROM Person WHERE id = ?
"""

person_sql_script_delete_all = """
    DELETE FROM Person
"""

person_sql_script_select_by_login = """
    SELECT * FROM Person WHERE login = ?
"""

