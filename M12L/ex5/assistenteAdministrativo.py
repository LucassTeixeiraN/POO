class AssistenteAdministrativo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Assistente Administrativo: {self.nome}, Idade: {self.idade}'