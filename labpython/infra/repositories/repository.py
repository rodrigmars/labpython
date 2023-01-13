from typing import Dict, Tuple, List, Callable, Any
from labpython.infra.db.sqlite_db import create_connection, close_connection

def repository(config:dict) -> Dict[str, Callable]:

    def send_log(message, error):
        print(message, error)
        pass

    def execute(query, params, mode) -> Any:
        
        conn = None

        data: Any = None

        try:
            
            conn = create_connection(config.get("PATH_DB_SQLITE", ""))
            
            cur = conn.cursor()

            cur.execute(query, params)


            if mode in ("create","update", "delete"):

                conn.commit()    

                if "create" == mode:
                    data = cur.rowcount

            if mode == "one":

                data = cur.fetchone()
        
            if mode == "all":
                
                data = cur.fetchall()
            
            if mode == "many":

                data = cur.fetchmany(5)


        except Exception as ex:

            send_log("ERRO >>>>>>>:", ex)

        finally:

            close_connection(conn)

            return data

    def create(query: str, params: dict) -> int:
        return execute(query, params, mode="create")

    def find(query: str, params: dict) -> Tuple:
        return execute(query, params, mode="one")

    def all(query: str, params: dict) -> List:
        return execute(query, params, mode="all")

    def edit(query: str, params: dict) -> None:
        return execute(query, params, mode="update")

    def remove(query: str, params: dict) -> None:
        return execute(query, params, mode="delete")

    return {"create": create, "find": find, "all": all, "edit": edit, "remove": remove}
