import os
from sqlite3 import Connection, Cursor
from typing import Dict
from labpython.db import create

class Login:

    def __init__(self, username, email, password, phone) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone


def insert(login: Login) -> int:
    """
    Cadastro login adotando estilo nomeado "named style" na instrução INSERT.
    Adotando uma abordagem como espaços reservados "placeholders" 
    ou pontos de interrogação "qmark style", 
    pode induzir a erros e falhas de segurança
    """

    conn: Connection = create(os.path.join("db", "camp.db"))

    row_id: int = 0

    try:

        query = """
            INSERT INTO logins (username, email, password, phone) 
            VALUES (:username, :email, :password, :phone);
            """

        cur: Cursor = conn.cursor()

        cur.execute(query, login.__dict__)

        conn.commit()

        row_id = cur.lastrowid or 0

    except Exception as e:
        raise Exception("erro", e)

    finally:
        conn.close()

        return row_id


def find_by_username(username: str) -> Dict[str, str]:

    conn: Connection = create(os.path.join("db", "camp.db"))

    query = f"""
    SELECT * FROM logins WHERE username=:username;
    """
    login: dict = {}

    try:

        cur: Cursor = conn.cursor()

        cur.execute(query, {"username": username})

        login = cur.fetchone()

    except Exception as e:
        raise Exception("erro", e)

    finally:

        conn.close()

        return login
