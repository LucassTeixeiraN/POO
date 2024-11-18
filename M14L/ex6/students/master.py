from .student import Student

class Master(Student):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Mestrado: {self.nome}'

    def estudar(self):
        print(f'{self.nome} está estudando para o mestrado.')