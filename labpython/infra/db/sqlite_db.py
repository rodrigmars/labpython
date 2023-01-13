from sqlite3 import Connection, connect

def create_connection(database: str) -> Connection:
  
  conn = connect(database)

  conn.set_trace_callback(print)
  
  return conn 


def close_connection(conn) -> None:
  conn.close()