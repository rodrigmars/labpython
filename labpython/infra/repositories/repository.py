import enum
from typing import Dict, Tuple, List, Callable, Any
from labpython.infra.db.sqlite_db import create_connection, close_connection

def repository(config:dict) -> Dict[str, Callable]:

    def send_log(message, error):
        print(message, error)
        pass

    class CurType(enum.Enum):
        CREATE = 1
        ONE = 2
        ALL = 3
        MANY = 4
        UPDATE = 5
        DELETE = 6

    
    def execute(query, params, cur_type:CurType) -> Any:
        
        conn = None

        data: Any = None

        try:
            
            conn = create_connection(config.get("PATH_DB_SQLITE", ""))
            
            cur = conn.cursor()

            cur.execute(query, params)


            if cur_type in (CurType.CREATE, CurType.UPDATE, CurType.DELETE):

                conn.commit()    

                if CurType.CREATE == cur_type:
                    data = cur.rowcount

            if cur_type == CurType.ONE:

                data = cur.fetchone()
        
            if cur_type == CurType.ALL:
                
                data = cur.fetchall()
            
            if cur_type == CurType.MANY:

                data = cur.fetchmany(5)


        except Exception as ex:

            send_log("ERRO >>>>>>>:", ex)

        finally:

            close_connection(conn)

            return data

    def create(query: str, params: dict) -> int:
        return execute(query, params, CurType.CREATE)

    def find(query: str, params: dict) -> Tuple:
        return execute(query, params, CurType.ONE)

    def all(query: str, params: dict) -> List:
        return execute(query, params, CurType.ALL)

    def edit(query: str, params: dict) -> None:
        return execute(query, params, CurType.UPDATE)

    def remove(query: str, params: dict) -> None:
        return execute(query, params, CurType.DELETE)

    return {"create": create, "find": find, "all": all, "edit": edit, "remove": remove}
