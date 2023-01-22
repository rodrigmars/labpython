import traceback
import logging
import sqlite3
from datetime import datetime
from typing import Optional

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
        :: %(message)s', level=logging.INFO, filename='databot.log')


def loginUseCase(cur: sqlite3.Cursor):

    def create(email: str, access_date: datetime) -> int | None:

        print("access_date>>>>>>>", access_date)

        cur.execute("INSERT INTO LOGIN_AUDIT(EMAIL, ACCESS_DATE) VALUES(:EMAIL, :ACCESS_DATE);",
                    (email, access_date))

        return cur.lastrowid

    def find_by_id(id: int) -> tuple:

        cur.execute("SELECT * FROM LOGIN_AUDIT WHERE ID=:ID", (id,))

        return cur.fetchone()

    def get_last_row_id():
        
        cur.execute("SELECT MAX(ROWID) FROM LOGIN_AUDIT;")

        return cur.fetchone()
        

    return {"create": create,
            "find_by_id": find_by_id,
            "get_last_row_id": get_last_row_id}

def main(conn: sqlite3.Connection, cur: sqlite3.Cursor, data:list) -> None:
    """
    Proof-of-Concept (PoC) para operações em memória no gerenciamento de login
    """

    email = 'test@gmail.com'
    
    access_date = datetime.strptime(
        "2018-06-21 12:15:28", "%Y-%m-%d %H:%M:%S")

    # .strftime("%m/%d/%Y, %H:%M:%S") datetime.timestamp(datetime.now())

    login_ = loginUseCase(cur)

    row_id = login_["create"](email, access_date)

    conn.commit()

    last_row_id = login_["get_last_row_id"]()

    print(f"last_row_id:{last_row_id}")

    if row_id:
        login = login_["find_by_id"](row_id)

        print(login)


def cerca_copione() -> tuple | None:

    data = list('teste')

    return (1, data) if data != [] else None

if __name__ == "__main__":

    conn: Optional[sqlite3.Connection] = None
    
    query = ""
    DB_TEMP = ""
    RELOAD = 1

    try:

        if not (trailer := cerca_copione()) is None:

            conn = sqlite3.connect(DB_TEMP)

            cur = conn.cursor()

            if RELOAD == trailer[0]:
                query = "DROP TABLE IF EXISTS LOGIN_AUDIT;\n"
                
            query += """CREATE TAB5LE IF NOT EXISTS LOGIN_AUDIT(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EMAIL TEXT NOT NULL UNIQUE,
            ACCESS_DATE TEXT NOT NULL,
            CHECK(LENGTH(EMAIL) > 0 AND EMAIL LIKE '%___@___%.__%')
            CHECK(ACCESS_DATE IS strftime('%Y-%m-%d %H:%M:%S', ACCESS_DATE)));
            \n
            """

            cur.executescript(query)

            main(conn, cur, trailer[1])
        
        else:
            logging.info("Não existem dados para processamento")

    except Exception:
        logging.error(traceback.format_exc())

    finally:

        if conn:
            conn.close()
