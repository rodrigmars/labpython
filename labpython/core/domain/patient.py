
class Patient():

    def __init__(self, name, email, cpf, birth_date, zip_code, number, id=None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.birth_date = birth_date
        self.zip_code = zip_code
        self.number = number
