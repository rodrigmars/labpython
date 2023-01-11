import sys
from infra.repositories.login_repository import repository
from entities.login import Login
from dotenv import dotenv_values


def main(config: dict):

    login = Login(username="rena2nmonteiro",
                  email="renanmon2teiro@bluewash.com.br",
                  password="rI0iqUj2brP",
                  phone="(66) 98201-0787")

    create, find = repository(config)

    create(login)

    sault = find("renanmonteiro")

    print(sault)


if __name__ == "__main__":

    rc = 1
    try:

        main(dotenv_values(".env"))

        rc = 0

    except Exception as e:

        print(f'Error: {e}', file=sys.stderr)

    sys.exit(rc)
