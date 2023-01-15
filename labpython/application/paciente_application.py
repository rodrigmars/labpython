from labpython.domain.entities.patient import Patient
from domain.value_objects.enum_vo import Operation
from typing import Callable, Tuple, Any

Repository = Callable[[dict[str, str]], Tuple[Callable[[
    str, Patient], int], Callable[[str], Tuple[int, str]]]]


def application(repository: Callable[[str, dict, Operation], Any]):

    def create(patient: Patient) -> int:

        query: str = """
                INSERT INTO PATIENTS (code, name, birth_date)
                VALUES (:code, :name, :birth_date);
                """
        return repository(query, patient.__dict__, Operation.Create)

    def find_by_code(code: str) -> int:
        
        query: str = "SELECT * FROM PATIENTS WHERE CODE =:code"

        return repository(query, {"code": code}, Operation.Find)

    return {"create": create, "find": find_by_code}
