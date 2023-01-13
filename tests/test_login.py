import pytest
from dotenv import dotenv_values
from typing import Iterator, Tuple, Any
from labpython.infra.db.sqlite_db import create_connection
from labpython.domain.entities.login import Login
from labpython.infra.repositories.repository import repository
from labpython.application.login_application import application


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


# Setup =  Tuple[Dict[str, Optional[str]], Connection, Login]
Setup = Tuple[Any, Login]
# Setup =  Login


def create_table(path_db_sqlite: str):

    conn = create_connection(path_db_sqlite)

    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS logins;")

    cur.execute(create_table_logins())

    conn.close()


@pytest.fixture(scope="function")
def setup() -> Iterator[Setup]:

    print("REPETINDO AQUI")

    # ARRANJO
    config = dotenv_values(".env")

    create_table(config.get("PATH_DB_SQLITE") or "")

    conn = create_connection(config.get("PATH_DB_SQLITE") or "")

    yield conn, Login(username="renanmonteiro",
                      email="renanmonteiro@bluewash.com.br",
                      password="rI0iqUjbrP",
                      phone="(66) 98201-0887")

    # conn.close()

# def test_create_login(setup: Setup):
#     #action
#     login, config = setup

#     create, _ = repository(config)

#     row_id: int = create(login)

#     assert row_id.__eq__(1)

# def test_select_login(setup: Setup):

#     login, config = setup

#     username = "renanmonteiro"

#     create, find = repository(config)

#     create(login)

#     result = find(username)

#     assert result[1].__eq__(username)

# def test_create_login_vs1(setup: Setup):

#     conn, login = setup

#     fn = domain(repository(conn))

#     conn.commit()

#     assert fn.__getitem__("create")(login).__eq__(1)


def test_create_login_vs1(setup: Setup):

    conn, login = setup

    row_id: int = 0

    try:

        row_id = application(repository(conn))["create"](login)

        conn.commit()

    except Exception as ex:

        print("1 - ERRO:::::::::::::", ex)

    finally:
        conn.close()
        assert row_id == 1


def test_create_login_vs2(setup: Setup):

    conn, login = setup

    row_id: int = 0

    try:

        row_id = application(repository(conn))["create"](login)

        conn.commit()

    except Exception as ex:

        print("2 - ERRO:::::::::::::", ex)

    finally:
        conn.close()
        assert row_id == 1
