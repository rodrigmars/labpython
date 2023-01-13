from typing import Dict, Tuple, List, Callable
from labpython.infra.db.sqlite_db import create_connection, close_connection

def repository(config:dict) -> Dict[str, Callable]:
    

    def create(query: str, params: dict) -> int:

        conn = None

        row_id: int = 0

        try:

            conn = create_connection(config.get("PATH_DB_SQLITE", ""))

            cur = conn.cursor()

            cur.execute(query, params)

            conn.commit()

            row_id = cur.rowcount

        except Exception as ex:
            # TO-DO Criar log funcional
            print("ERRO >>>>>>>:", ex)
        finally:

            close_connection(conn)

            return row_id

    def find(query: str, data: dict) -> Tuple[int, str, str]:
        return 1, "", ""

    def all() -> List[int]:
        return [1, 2, 3, 4]

    def edit() -> Tuple[int, str]:
        return 1, ""

    def remove() -> None:
        pass

    return {"create": create, "find": find, "all": all}
