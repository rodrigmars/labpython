import sys
from typing import Optional
from dotenv import dotenv_values
from application.login_application import application
from domain.entities.login import Login
from infra.repositories.repository import repository
from infra.db.sqlite_db import Connection, Cursor, create_connection


def main(config: dict, conn: Connection, cur: Cursor) -> None:

    login = Login(username="rena2nmonteiro",
                  email="renanmon2teiro@bluewash.com.br",
                  password="rI0iqUj2brP",
                  phone="(66) 98201-0787")

    fn = application(repository(cur))

    fn["create"](login)

    conn.commit()

    result = fn["find_by_username"]("renanmonteiro")

    print(result)


if __name__ == "__main__":

    rc = 1
    
    conn: Optional[Connection] = None
 
    try:

        config = dotenv_values(".env")

        if path_db := config.get("PATH_DB_SQLITE"):

            conn, cur = create_connection(path_db)

            main(config, conn, cur)

            rc = 0

        else:
            raise Exception("Unable to connect to data source undefined")

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)

    finally:
        if conn:
            conn.close()

        sys.exit(rc)
