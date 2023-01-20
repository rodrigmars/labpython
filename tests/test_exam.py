from pytest import mark, param, raises as sqliteRaises
from datetime import date
from typing import Tuple, Callable, Union, List
from sqlite3 import Connection, Cursor, Error

Setup = Tuple[Connection, Cursor, Callable[[int], str]]


def test_to_create_and_verify_exams(setup: Setup):

    conn, cur, gen_code = setup

    sql_insert = """
    INSERT INTO EXAM(CODE, TYPE, DESCRIPTION, PRICE)
    VALUES(:CODE, :TYPE, :DESCRIPTION, :PRICE)
    """
    sql_select = "SELECT CODE FROM PATIENT WHERE ID =:ID;"

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

    expected = 3

    cur.executemany(sql_insert, exams)

    conn.commit()

    assert expected >= len(cur.execute(sql_select,
                                       (cur.lastrowid,)).fetchall())



# @mark.skip(reason="")
def test_to_edit_price_and_last_update_exams(setup: Setup):

    conn, cur, gen_code = setup

    sql_insert = """
    INSERT INTO EXAM(CODE, TYPE, DESCRIPTION, PRICE)
    VALUES(:CODE, :TYPE, :DESCRIPTION, :PRICE)
    """
    sql_update = """
    UPDATE EXAM SET LAST_UPDATE=CURRENT_TIMESTAMP, PRICE =:PRICE WHERE CODE =:CODE;
    """
    sql_select = "SELECT PRICE FROM EXAM WHERE CODE =:CODE;"

    exams: Tuple[str, str, str, float] = (code := gen_code(8), "Hematologia", "Análise de plaquetas,\
                                         leucócitos, hemácias, entre outros, \
                                            feita a partir da coleta de sangue", 95.0)

    expected = 150.0

    cur.execute(sql_insert, exams)

    cur.execute(sql_update, (expected, code))

    conn.commit()

    cur.execute(sql_select, (code,))

    assert expected == cur.execute(sql_select,
                                   (code,)).fetchone()[0]


# @mark.skip(reason="")
def test_to_delete_exams(setup: Setup):

    conn, cur, gen_code = setup

    sql_insert = """
    INSERT INTO EXAM(CODE, TYPE, DESCRIPTION, PRICE)
    VALUES(:CODE, :TYPE, :DESCRIPTION, :PRICE)
    """

    sql_delete = "DELETE FROM EXAM WHERE CODE =:CODE;"

    sql_select = "SELECT * FROM EXAM WHERE CODE =:CODE;"

    exams: Tuple[str, str, str, float] = (code := gen_code(8), "Hematologia",
                                          "Análise de plaquetas, leucócitos, hemácias, entre outros, feita a partir da coleta de sangue",
                                          115.5)

    cur.execute(sql_insert, exams)

    cur.execute(sql_delete, (code,))

    conn.commit()

    assert cur.execute(sql_select, (code,)).fetchone() is None


# def get_limited_rows(size):
#     try:
#         connection = sqlite3.connect(':memory:')
#         cursor = connection.cursor()

#         query = """SELECT * from table"""
#         cursor.execute(query)
#         records = cursor.fetchmany(size)

#         cursor.close()

#     except sqlite3.Error as error:
#         print("FAILED:", error)
#     finally:
#         if connection:
#             connection.close()



# def test_to_delete_exams(setup: Setup):

#     with sqliteRaises(Exception) as e_info:
#         conn, cur, gen_code = setup

#         sql_insert = """
#         INSERT INTO EXAM(CODE, TYPE, DESCRIPTION, PRICE)
#         VALUES(:CODE, :TYPE, :DESCRIPTION, :PRICE)
#         """

#         sql_delete = """
#             DELETE FROM EXAM WHERE CODE =:CODE;
#         """

#         sql_select = "SELECT * FROM EXAM WHERE CODE =:CODE;"

#         exams: Tuple[str, str, str, str] = (code := gen_code(8), "Hematologia",
#                                                      "Análise de plaquetas, leucócitos, hemácias, entre outros, feita a partir da coleta de sangue",
#                                                      "25.8")


#         cur.execute(sql_insert, exams)

#         conn.commit()

#         cur.execute(sql_select, (code,))

#         print(">>>>>>>>>>>>>>>>>", cur.execute(sql_select, (code,)).fetchone())

    

#     assert str(e_info.value).__eq__("NOT NULL constraint failed: EXAM.price")

