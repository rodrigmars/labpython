from datetime import date
from typing import Tuple, Callable, Union
from sqlite3 import Connection, Cursor

Setup = Tuple[Connection, Cursor, Callable[[int], str]]

def test_create(setup: Setup):

    conn, cur, gen_code = setup

    query = """
    INSERT INTO PATIENT(code, name, birth_date) 
    VALUES(:code, :name, :birth_date)"""

    patient: dict[str, Union[str, str, date]] = {"code": gen_code(8),
                                                 "name": "Mariane Bárbara da Silva",
                                                 "birth_date": date(2002, 12, 31)}

    cur.execute(query, patient)

    conn.commit()

    cur.execute("SELECT CODE FROM PATIENT WHERE ID =:ID;",
                (cur.lastrowid,))

    assert cur.fetchone()[0] == patient.get("code")
