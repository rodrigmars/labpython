from typing import Callable, Any
from infra.db.sqlite_db import Connection
from domain.value_objects.enum_vo import Operation

def repository(conn: Connection) -> Callable[[str, dict, Operation], Any]:

    cur = conn.cursor()

    def execute(query: str, params: dict, operation: Operation):

        data: Any = None

        cur.execute(query, params)

        match operation:
            case Operation.Create:
                data = cur.rowcount
            case Operation.Find:
                data = cur.fetchone()
            case Operation.All:
                data = cur.fetchall()

        return data

    return execute
