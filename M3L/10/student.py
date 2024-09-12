# 10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
# Student. Um método deve testar a igualdade. Um segundo método deve testar para
# menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
# método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
# função main que testa todos os operadores de comparação. Em seguida, coloque
# vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
# com esta lista e exiba todas as informações dos alunos.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getName(self):
        return self.name

    def equal(self, anotherStudent):
        if self.grade == anotherStudent.grade:
            return True
        return False

    def greaterThan(self, anotherStudent):
        if self.grade > anotherStudent.grade:
            return True
        return False
    
    def lessThan(self, anotherStudent):
        if self.grade < anotherStudent.grade:
            return True
        return False

    def checkGrade(self, grade):
        if self.grade == grade:
            return True
        return False
        
