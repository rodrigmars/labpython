from sqlite3 import Cursor
from typing import Any, Callable, Dict

def patient_repository(cur: Cursor) -> Dict[str, Callable]:

    def create(patient: list[str]):

        cur.execute("""INSERT INTO Paciente(NOME, CPF, DATA_NASCIMENTO, ENDERECO) 
        VALUES(:NOME, :CPF, :DATA_NASCIMENTO, :ENDERECO);""", patient)

    def all() -> list[Any]:

        query = "SELECT * FROM Paciente;"

        cur.execute(query)

        return cur.fetchall()

    def find_by_name(name: str) -> tuple:

        return 5,

    def edit(id: int, patient: tuple[str]):
        pass

    def delete(id: int) -> None:
        pass

    return {"create": create,
            "all": all,
            "find_by_name": find_by_name,
            "edit": edit,
            "delete": delete}
