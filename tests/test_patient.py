from datetime import date
from typing import Tuple, Callable, Union
from sqlite3 import Connection, Cursor

Setup = Tuple[Connection, Cursor, Callable[[int], str]]

def test_to_create_and_verify_a_patient(setup: Setup):

    conn, cur, gen_code = setup

    sql = {"insert": """
    INSERT INTO PATIENT(code, name, birth_date) 
    VALUES(:code, :name, :birth_date)
    """, "select": "SELECT CODE FROM PATIENT WHERE ID =:ID;"}


    patient: dict[str, Union[str, str, date]] = {"code": (code := gen_code(8)),
                                                 "name": "Mariane Bárbara da Silva",
                                                 "birth_date": date(2002, 12, 31)}

    cur.execute(sql["insert"], patient)

    conn.commit()

    cur.execute(sql["select"], (cur.lastrowid,))

    assert cur.fetchone()[0] == code

def test_to_edit_name_and_birth_date_to_patient(setup: Setup):

    conn, cur, gen_code = setup

    sql = {"insert": """
    INSERT INTO PATIENT(code, name, birth_date) 
    VALUES(:code, :name, :birth_date)""",
              "update": "UPDATE PATIENT SET NAME =:NAME, BIRTH_DATE =:BIRTH_DATE WHERE CODE =:CODE",
              "select": "SELECT NAME, BIRTH_DATE FROM PATIENT WHERE CODE =:CODE;"}

    patient: dict[str, Union[str, str, date]] = {"code": (code := gen_code(8)),
                                                 "name": "Mariane Bárbara",
                                                 "birth_date": date(2002, 12, 31)}

    cur.execute(sql["insert"], patient)

    edit_patient: dict[str, Union[str, str, date]] = {"code": code,
                                                        "name": "Mariane Bárbara da Silva",
                                                        "birth_date": date(2000, 5, 15)}

    cur.execute(sql["update"], (edit_patient['name'],
                        edit_patient['birth_date'],
                        edit_patient["code"]))

    conn.commit()

    cur.execute(sql["select"], (patient.get("code"),))

    assert (result := cur.fetchone())[0] == edit_patient["name"]  \
        and edit_patient["birth_date"].__str__() == result[1]
