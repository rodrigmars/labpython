import pytest
from dotenv import dotenv_values
from typing import Iterator, Optional, Dict, Tuple, List, Callable
from labpython.infra.db.sqlite_db import create_connection, close_connection
from labpython.entities.login import Login
from labpython.infra.repositories.login_repository import repository
from labpython.domain.login_domain import domain


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
    
    #ARRANJO

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
    #action
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


def repository_(config) -> Dict[str, Callable]:
    
    db_local = config.get("PATH_DB_SQLITE") or ""
    
    def create(query: str, login: dict) -> int:
        return 1

    def find(query: str, data: dict) -> Tuple[int, str, str]:
        return 1, "", ""

    def all() -> List[int]:
        return [1, 2, 3, 4]

    def edit() -> Tuple[int, str]:
        return 1, ""

    def remove() -> None:
        pass

    return {"create": create, "find": find, "all": all}

def domain(repository: Dict[str, Callable]):

    def create(login: Login) -> int:

        query: str = """
                INSERT INTO logins (username, email, password, phone) 
                VALUES (:username, :email, :password, :phone);
                """
        return repository.__getitem__("create")(query, login.__dict__)

    def find_by_username(username: str) -> int:
        
        query: str = "SELECT USERNAME, EMAIL FROM LOGIN WHERE USERNAME=:username"

        return repository.__getitem__("find")(query, {"username": username})

    return {"create": create, "find_by_username": find_by_username}

def test_create_login_vs1(setup: Setup):

    login, config = setup

    fn = domain(repository_(config))

    assert fn.__getitem__("create")(login).__eq__(1)

def test_create_login_vs2(setup: Setup):

    login, config = setup

    assert domain(repository_(config))["create"](login).__eq__(1)
