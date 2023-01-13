from typing import Tuple
from infra.db.sqlite_db import create_connection
from entities.login import Login


def repository(config: dict):
    
    path_db_sqlite: str = config.get("PATH_DB_SQLITE") or ""

    def insert(login: Login) -> int:
        """
        Cadastro login adotando estilo nomeado "named style" na instrução INSERT.
        Adotando uma abordagem como espaços reservados "placeholders" 
        ou pontos de interrogação "qmark style", 
        pode induzir a erros e falhas de segurança
        """

        conn = create_connection(path_db_sqlite)

        row_id: int = 0

        try:

            query = """
                INSERT INTO logins (username, email, password, phone) 
                VALUES (:username, :email, :password, :phone);
                """

            repository.create(query)


            cur = conn.cursor()

            cur.execute(query, login.__dict__)

            conn.commit()

            row_id = cur.lastrowid or 0

        except Exception as e:
            raise Exception("erro", e)

        finally:
            conn.close()

            return row_id


    def find_by_username(username: str) -> Tuple[int, str]:

        conn = create_connection(path_db_sqlite)

        query = f"""
        SELECT * FROM logins WHERE username=:username;
        """
        login: tuple = ()

        try:

            cur = conn.cursor()

            cur.execute(query, {"username": username})

            login = cur.fetchone()

        except Exception as e:
            raise Exception("erro", e)

        finally:

            conn.close()

            return login

    return insert, find_by_username