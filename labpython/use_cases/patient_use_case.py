from typing import Callable, Dict, Tuple

def check_patients(f):
    """Decorator that prints Hello!"""
    def func(*args, **kwargs):

        notifys = []

        for list in args:
            if list[0] == "":
                notifys.append("Campo 'nome' necessário")
            if list[1] == "":
                notifys.append("Campo 'cpf' necessário")
            if list[2] == "":
                notifys.append("Campo 'data_nascimento' necessário")
            if list[3] == "":
                notifys.append("Campo 'endereco' necessário")

        if notifys != []:
            raise ValueError(notifys)

        return f(*args, **kwargs)

    return func

def insert_new_patient(repository: Dict[str, Callable]) -> Tuple[Callable]:

    @check_patients
    def create(patients: list[str]):
        repository["create"](patients)

    return create,
