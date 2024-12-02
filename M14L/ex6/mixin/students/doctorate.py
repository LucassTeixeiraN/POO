from .student import Student

class Doctorate(Student):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Doutorado: {self.nome}'

    def estudar(self):
        self.notify(f"{self.nome}, boa sorte nos estudos para o doutorado!")
        print(f'{self.nome} está estudando para o doutorado.')
