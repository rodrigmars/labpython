from typing import Dict, Tuple, List, Callable
from labpython.infra.db.sqlite_db import create_connection, close_connection

def repository(config:dict) -> Dict[str, Callable]:

    def send_log(message, error):
        print(message, error)
        pass

    def execute(query, params):
        
        conn = None        
        row_id: int = 0
        try:

            conn = create_connection(config.get("PATH_DB_SQLITE", ""))

            cur = conn.cursor()

            cur.execute(query, params)

            conn.commit()

            row_id = cur.rowcount

        except Exception as ex:

            send_log("ERRO >>>>>>>:", ex)

        finally:

            close_connection(conn)

            return row_id

    def execute_query(query, params):
        return "",

    def create(query: str, params: dict) -> int:
        return execute(query, params)

    def find(query: str, params: dict):
        return execute_query(query, params)

    def all(query: str, params: dict):
        return execute_query(query, params)

    def edit(query: str, params: dict) -> None:
        execute(query, params)

    def remove(query: str, params: dict) -> None:
        execute(query, params)

    return {"create": create, "find": find, "all": all, "edit": edit, "remove": remove}
