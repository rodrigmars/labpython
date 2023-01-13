from entities.login import Login
from typing import Callable, Tuple, Dict

Repository = Callable[[dict[str, str]], Tuple[Callable[[
    str, Login], int], Callable[[str], Tuple[int, str]]]]

def domain(repository: Dict[str, Callable]):

    def create(login: Login) -> int:

        query: str = """
                INSERT INTO logins (username, email, password, phone) 
                VALUES (:username, :email, :password, :phone);
                """

        # return repository.__getitem__("create")(query, login.__dict__)
        return repository["create"](query, login.__dict__)

    def find_by_username(username: str) -> int:
        
        query: str = "SELECT USERNAME, EMAIL FROM LOGIN WHERE USERNAME=:username"

        return repository.__getitem__("find")(query, {"username": username})

    return {"create": create, "find_by_username": find_by_username}
