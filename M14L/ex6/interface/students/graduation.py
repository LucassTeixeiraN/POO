from .student import Student

class Graduation(Student):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Graduação: {self.nome}'

    def estudar(self):
        print(f'{self.nome} está estudando para a sua graduação')
        