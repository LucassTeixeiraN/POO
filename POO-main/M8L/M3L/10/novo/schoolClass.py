from student import Student
import random

class schoolClass:
    # O atributo __students é uma lista de classes, então toda vez que ele é chamado o código está trabalhando com um objeto
    # sendo assim, há uma injeção de dependência entre essas classes
    def __init__(self, students):
        self.__students = students
        self.studentsOrdenate(self.__students)

    def addStudent(self, student: Student):
        self.__students.append(student)
    
    def setStudents(self, list):
        self.__students = list

    def getStudents(self):
        return self.__students

    @staticmethod
    def studentsOrdenate(list):
        random.shuffle(list)
        list.sort()

    @staticmethod
    def compareStudents(student1, student2):
        if student1 == student2:
            print("Os alunos tiraram a mesma nota")
        if student1 > student2:
            print(f"O aluno {student1.getName()} (número {student1.getNumber()}) tirou a maior nota")
        if student1 < student2:
            print(f"O aluno {student2.getName()} (número {student2.getNumber()}) tirou a maior nota")

    def __str__(self):
        for i in self.__students:
            print(f"O aluno {i.getName()}(número {i.getNumber()}) tirou {i.getGrade()}")
        print("-"*60)
