from .student import Student

class Master(Student):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Mestrado: {self.nome}'

    def estudar(self):
        print(f'{self.nome} está estudando para o mestrado.')