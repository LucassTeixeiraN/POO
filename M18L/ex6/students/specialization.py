from .student import Student

class Specialization(Student):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Especialização: {self.nome}'

    def estudar(self):
        print(f'{self.nome} está estudando para a sua especialização')