from sqlite3 import Connection, connect


def create(database: str) -> Connection:
  return connect(database)


def close(conn) -> None:
  conn.close()