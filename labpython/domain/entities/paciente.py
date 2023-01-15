class Paciente:

    def __init__(self, codigo, nome, data_nascimento) -> None:
        self.id = None
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.last_update = None
