import os
import pytest
from dotenv import dotenv_values
from typing import Iterator, Optional, Dict, Tuple
from labpython.infra.db.sqlite_db import create_connection, close_connection
from labpython.entities.login import Login
from labpython.infra.repositories.login_repository import repository


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
Setup =  Tuple[Login, Dict[str, Optional[str]]]

@pytest.fixture(scope="function")
def setup() -> Iterator[Setup]:

    config = dotenv_values(".env")

    path_db_sqlite = config.get("PATH_DB_SQLITE") or ""

    conn = create_connection(path_db_sqlite)

    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS logins;")

    cur.execute(create_table_logins())

    close_connection(conn)
    
    yield Login(username="renanmonteiro",
                email="renanmonteiro@bluewash.com.br",
                password="rI0iqUjbrP",
                phone="(66) 98201-0887"), config

def test_create_login(setup: Setup):

    login, config = setup

    create, _ = repository(config)

    row_id: int = create(login)

    assert row_id.__eq__(1)

def test_select_login(setup: Setup):

    login, config = setup

    username = "renanmonteiro"

    create, find = repository(config)

    create(login)

    result = find(username)

    assert result[1].__eq__(username)
