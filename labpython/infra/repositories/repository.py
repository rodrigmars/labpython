from typing import Callable, Any
from infra.db.sqlite_db import Cursor
from domain.value_objects.enum_vo import Operation


def repository(cur: Cursor) -> Callable[[str, dict, Operation], Any]:

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
