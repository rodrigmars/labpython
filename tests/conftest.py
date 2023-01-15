import pytest
from enum import Enum
from labpython.infra.db.sqlite_db import create_connection
from dotenv import dotenv_values
from typing import Tuple, Callable, Any

CreateTables = Tuple[Any, str]

def query_create_table_patients() -> str:

    return """CREATE TABLE PATIENTS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL UNIQUE,
        birth_date DATETIME NOT NULL,
        event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        last_update DATETIME NULL);"""

def query_create_table_exams() -> str:

    return """CREATE TABLE EXAMS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_update DATETIME NULL);"""

def query_create_table_patients_exams() -> str:

    return """CREATE TABLE PATIENTS_EXAMS ( 
            id_patients INTEGER NOT NULL,  
            id_exams    INTEGER NOT NULL,
            FOREIGN KEY(id_patients) REFERENCES PATIENTS(id),
            FOREIGN KEY(id_exams) REFERENCES EXAMS(id));"""

class Tables(Enum):
    PATIENTS = 1
    EXAMS = 2
    PATIENTS_EXAMS = 3

def create_tables(path_db: str, fn: Any, tables: Tables) -> None:

    conn = create_connection(path_db)

    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS PATIENTS;")
    cur.execute("DROP TABLE IF EXISTS EXAMS;")
    cur.execute("DROP TABLE IF EXISTS PATIENTS_EXAMS;")

    match tables:

        case Tables.PATIENTS:
            cur.execute(fn())

        case Tables.EXAMS:
            cur.execute(fn())

        case Tables.PATIENTS_EXAMS:
            table_patients, table_exams, table_patients_exams = fn

            cur.execute(table_patients())
            cur.execute(table_exams())
            cur.execute(table_patients_exams())

    conn.close()

# Arrange
@pytest.fixture
def setup_patients():

    config = dotenv_values(".env")

    path_db = config.get("PATH_DB_SQLITE") or ""

    create_tables(path_db=path_db,
                  fn=query_create_table_patients,
                  tables=Tables.PATIENTS)

    conn = create_connection(path_db)
    
    yield conn, config

    conn.close()


@pytest.fixture
def setup_exams():

    config = dotenv_values(".env")

    path_db = config.get("PATH_DB_SQLITE") or ""

    create_tables(path_db=path_db,
                  fn=query_create_table_exams,
                  tables=Tables.EXAMS)

    conn = create_connection(path_db)
    
    yield conn, config

    conn.close()


@pytest.fixture
def setup_patients_exams():

    config = dotenv_values(".env")

    path_db = config.get("PATH_DB_SQLITE") or ""

    create_tables(path_db=path_db,
                  fn=(query_create_table_patients,
                             query_create_table_exams,
                             query_create_table_patients_exams),
                  tables=Tables.PATIENTS_EXAMS)


    conn = create_connection(path_db)
    
    yield conn, config

    conn.close()
