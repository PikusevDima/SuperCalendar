note_sql_script_create_table = """
    CREATE TABLE IF NOT EXISTS Note (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        text TEXT NOT NULL,
        person_id INTEGER NOT NULL
    )
"""

note_sql_script_insert = """
    INSERT INTO Note (name, text, person_id) VALUES (?, ?, ?)
"""

note_sql_script_select_all = """
    SELECT * FROM Note
"""

note_sql_script_delete_all = """
    DELETE FROM Note
"""

note_sql_script_delete_by_id = """
    DELETE FROM Note WHERE id = ? 
"""



