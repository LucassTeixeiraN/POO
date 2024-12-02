from .student import Student

class Graduation(Student):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Graduação: {self.nome}'

    def estudar(self):
        self.notify(f"{self.nome}, continue se dedicando à sua graduação!")
        print(f'{self.nome} está estudando para a sua graduação.')
