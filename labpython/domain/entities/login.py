class Login:

    def __init__(self, username, email, password, phone) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    def dict(self):
        return self.__dict__
