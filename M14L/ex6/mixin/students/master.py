from .student import Student

class Master(Student):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Mestrado: {self.nome}'

    def estudar(self):
        self.notify(f"{self.nome}, parabéns pela dedicação ao mestrado!")
        print(f'{self.nome} está estudando para o mestrado.')
