class Patient:

    def __init__(self, code, name, birth_date) -> None:
        self.id = None
        self.code = code
        self.name = name
        self.birth_date = birth_date
        self.last_update = None
