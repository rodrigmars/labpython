import pytest
import random
import string
from typing import Iterator, Tuple, Callable
from sqlite3 import connect, Connection, Cursor

Setupe = Iterator[Tuple[Connection, Cursor, Callable[[int], str]]]


def gen_code(digits: int) -> str:

    return ''.join(random.choices(string.ascii_uppercase + string.digits,
                                  k=digits))


def create_tables(cur) -> None:
    cur.executescript(
        """
        CREATE TABLE PATIENT(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL UNIQUE,
            birth_date DATETIME NOT NULL,
            event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_update DATETIME NULL);
        CREATE TABLE EXAM(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                type TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_update DATETIME NULL);
        CREATE TABLE PATIENT_EXAM ( 
            id_patients INTEGER NOT NULL,  
            id_exams    INTEGER NOT NULL,
            FOREIGN KEY(id_patients) REFERENCES PATIENTS(id),
            FOREIGN KEY(id_exams) REFERENCES EXAMS(id));
        """)

# Arrange
@pytest.fixture
def setup() -> Setupe:

    conn = connect(':memory:')

    cur = conn.cursor()

    create_tables(cur)

    yield conn, cur, gen_code

    conn.close()
