from typing import Callable, Dict, Tuple, Any, List
from core.domain.patient import Patient
from infra.email_sender import FactoryEmailSender

class PatientError(Exception):
    def __init__(self, function: str, message: Any):
        self.function = function
        self.message = message
        super().__init__(self.function, self.message)

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
            raise PatientError("check_patients", notifys)

        return f(*args, **kwargs)

    return func


def insert_new_patient(repository: Dict[str, Callable[[Any], Any]],
                       email_sender: FactoryEmailSender) -> Callable[[Patient], None]:
    """
    Verifica dados do novo paciente e dispara cadastro
    """

    def check_patient_code(cpf: str) -> None:
        if patient := repository["find_by"](cpf):
            raise PatientError("check_patient_code",
                               f"Já existe um cadastro para o usuário '{patient[0]}'")

    @check_patients
    def create(patient:Patient) -> None:

        check_patient_code(patient.cpf)

        repository["create"](patient)

        email_sender["confirm_new_password"](patient.name, patient.email)

    return create
