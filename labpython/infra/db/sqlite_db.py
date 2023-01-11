from sqlite3 import Connection, connect


def create_connection(database: str) -> Connection:
  return connect(database)


def close_connection(conn) -> None:
  conn.close()