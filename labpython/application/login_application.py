from domain.entities.login import Login
from domain.value_objects.enum_vo import Operation
from typing import Callable, Tuple, Any

Repository = Callable[[dict[str, str]], Tuple[Callable[[
    str, Login], int], Callable[[str], Tuple[int, str]]]]


def application(repository: Callable[[str, dict, Operation], Any]):

    def create(login: Login) -> int:

        query: str = """
                INSERT INTO logins (username, email, password, phone) 
                VALUES (:username, :email, :password, :phone);
                """
        return repository(query, login.dict(), Operation.Create)

    def find_by_username(username: str) -> int:

        query: str = "SELECT USERNAME, EMAIL FROM LOGINS WHERE USERNAME=:username"

        return repository(query, {"username": username}, Operation.Find)

    return {"create": create, "find_by_username": find_by_username}
