from entities.login import Login
from typing import Callable, Tuple

Repository = Callable[[dict[str, str]], Tuple[Callable[[
    str, Login], int], Callable[[str], Tuple[int, str]]]]


def domain(querys: Repository):

    insert, _ = querys

    def create(login: Login):

        query = """
                INSERT INTO logins (username, email, password, phone) 
                VALUES (:username, :email, :password, :phone);
                """

        insert(query, login)


    return create