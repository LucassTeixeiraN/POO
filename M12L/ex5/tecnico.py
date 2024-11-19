class Tecnico:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Técnico: {self.nome}, Idade: {self.idade}'