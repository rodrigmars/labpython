import pytest
from enum import Enum
from labpython.infra.db.sqlite_db import create_connection
from dotenv import dotenv_values
from typing import Tuple, Any

CreateTables = Tuple[Any, str]

def create_tables(path_db:str) -> None:

    conn = create_connection(path_db)

    cur = conn.cursor()

    cur.executescript(
        """
        BEGIN;
        DROP TABLE IF EXISTS PATIENTS;
        DROP TABLE IF EXISTS EXAMS;
        DROP TABLE IF EXISTS PATIENTS_EXAMS;
        CREATE TABLE PATIENTS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL UNIQUE,
            birth_date DATETIME NOT NULL,
            event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_update DATETIME NULL);
        CREATE TABLE EXAMS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_update DATETIME NULL);      
        CREATE TABLE PATIENTS_EXAMS ( 
            id_patients INTEGER NOT NULL,  
            id_exams    INTEGER NOT NULL,
            FOREIGN KEY(id_patients) REFERENCES PATIENTS(id),
            FOREIGN KEY(id_exams) REFERENCES EXAMS(id));
        COMMIT;
        """)

    conn.close()

# Arrange
@pytest.fixture
def setup_patients():

    config = dotenv_values(".env")

    path_db = config.get("PATH_DB_SQLITE") or ""

    create_tables(path_db)

    conn = create_connection(path_db)

    yield conn, config

    conn.close()