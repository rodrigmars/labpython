from typing import Tuple
from sqlite3 import Connection,Cursor, connect


def create_connection(database: str) -> Tuple[Connection, Cursor]:

  connection = connect(database)

  cursor = connection.cursor()

  connection.set_trace_callback(print)

  return connection, cursor
