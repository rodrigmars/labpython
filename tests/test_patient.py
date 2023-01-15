

def setupe():

    query = """CREATE TABLE PATIENTS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL UNIQUE,
        birth_date DATETIME NOT NULL,
        event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        last_update DATETIME NULL);"""
