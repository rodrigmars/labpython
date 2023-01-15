from domain.entities.exame import Exame
from domain.value_objects.enum_vo import Operation
from typing import Callable, Tuple, Any

Repository = Callable[[dict[str, str]], Tuple[Callable[[
    str, Exame], int], Callable[[str], Tuple[int, str]]]]


def application(repository: Callable[[str, dict, Operation], Any]):

    def create(exams: Exame) -> int:

        query: str = """
                INSERT INTO EXAMS (code, description, price) 
                VALUES (:code, :description, :price);
                """
        return repository(query, exams.__dict__, Operation.Create)

    def find_by_code(code: str) -> int:

        query: str = "SELECT * FROM EXAMS WHERE CODE =:code"

        return repository(query, {"code": code}, Operation.Find)

    return {"create": create, "find_by_code": find_by_code}
