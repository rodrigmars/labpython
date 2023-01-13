import sys
from infra.repositories.repository import repository
from domain.entities.login import Login
from application.login_application import application
from dotenv import dotenv_values
from infra.db.sqlite_db import Connection, create_connection


def main(config: dict, conn: Connection):

    login = Login(username="rena2nmonteiro",
                  email="renanmon2teiro@bluewash.com.br",
                  password="rI0iqUj2brP",
                  phone="(66) 98201-0787")

    fn = application(repository(conn))

    fn["create"](login)

    sault = fn["find_by_username"]("renanmonteiro")

    print(sault)


if __name__ == "__main__":

    rc = 1

    conn = None

    try:
        config = dotenv_values(".env")
        conn = create_connection(config.get("PATH_DB_SQLITE") or "")

        main(config, conn)

        rc = 0

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)

    finally:
        if conn:
            conn.close()

        sys.exit(rc)
