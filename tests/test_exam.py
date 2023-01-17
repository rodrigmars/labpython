from pytest import mark
from datetime import date
from typing import Tuple, Callable, Union, List
from sqlite3 import Connection, Cursor

Setup = Tuple[Connection, Cursor, Callable[[int], str]]

def test_to_create_and_verify_exams(setup: Setup):

    conn, cur, gen_code = setup

    sql_insert, sql_select = """
    INSERT INTO EXAM(CODE, TYPE, DESCRIPTION, PRICE)
    VALUES(:CODE, :TYPE, :DESCRIPTION, :PRICE)
    """, "SELECT CODE FROM PATIENT WHERE ID =:ID;"

    exams: List[Tuple[str, str, str, float]] = [
        (gen_code(8), "Hematologia",
         "Análise de plaquetas, leucócitos, hemácias, entre outros, feita a partir da coleta de sangue",
         95.5),
        (gen_code(8), "Bioquímica",
         "Para o controle de colesterol, diabetes, triglicérides, creatinina, entre outros.",
         120.5),
        (gen_code(8), "Microbiologia",
         "Para detectar infecções. Feito através da coleta de secreções.",
         175.0)]

    cur.executemany(sql_insert, exams)

    conn.commit()

    (total := len(cur.execute(sql_select, (cur.lastrowid,)).fetchall()))

    assert 3 >= total

@mark.skip(reason="")
def test_to_edit_name_and_birth_date_to_exams(setup: Setup):

    conn, cur, gen_code = setup
  
@mark.skip(reason="")
def test_to_delete_exams(setup: Setup):

    conn, cur, gen_code = setup