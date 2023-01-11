import os
import pytest
from typing import Iterator
from sqlite3 import Connection, Cursor
from labpython.infra.db import create, close
from labpython.entities.login import Login
from labpython.core.login_core import insert, find_by_username

def create_table_logins() -> str:
    return """
    CREATE TABLE logins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        last_update DATETIME NULL);
    """

@pytest.fixture(scope="function")
def setup() -> Iterator[Login]:

    conn: Connection = create(os.path.join("db", "camp.db"))

    cur: Cursor = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS logins;")

    cur.execute(create_table_logins())

    close(conn)

    yield Login(username="renanmonteiro",
                email="renanmonteiro@bluewash.com.br",
                password="rI0iqUjbrP",
                phone="(66) 98201-0887")


def test_create_login(setup: Login):

    login = setup

    row_id: int = insert(login)

    assert row_id.__eq__(1)

def test_select_login(setup: Login):

    login = setup

    username = "renanmonteiro"

    insert(login)

    result: dict = find_by_username(username)

    assert result.get("username", "").__eq__(username)
