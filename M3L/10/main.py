# 10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
# Student. Um método deve testar a igualdade. Um segundo método deve testar para
# menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
# método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
# função main que testa todos os operadores de comparação. Em seguida, coloque
# vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
# com esta lista e exiba todas as informações dos alunos.

from student import Student
import random

def menu():
    try:
        option = int(input("Escolha uma das opções:\n1- Comparar a nota de dois alunos\n2- Colocar as notas dos alunos em ordem crescente\n3- sair\n"))
        return option
    except ValueError:
        print("Valor inválido")
        menu() 

def newStudent(num):
    name = input(f"Nome do {num}° estudante: ")
    number = int(input(f"Número do {num}° estudante: "))
    grade = float(input(f"Nota do {num}° estudante: "))
    return Student(name, grade, number)

def compareStudents(student1, student2):
    if student1.__eq__(student2):
        print("Os alunos tiraram a mesma nota")
    if student1.__gt__(student2):
        print(f"O aluno {student1.getName()} (número {student1.getNumber()}) tirou a maior nota")
    if student1.__lt__(student2):
        print(f"O aluno {student2.getName()} (número {student2.getNumber()}) tirou a maior nota")

def listOrdenate(students):
    random.shuffle(students)
    students.sort()
    return students


def main():
    while True:
        option = menu()
        if option == 1:
            student1 =  newStudent(1)           
            student2 =  newStudent(2)           
        
            compareStudents(student1, student2)

        elif option == 2:
            studentsNum = int(input("Insira o número de alunos da turma: "))
            students = []
            for i in range(studentsNum):
                students.append(newStudent(i+1))
            listOrd = listOrdenate(students)
            print("-"*60)
            for i in listOrd:
                print(f"O aluno {i.getName()}(número {i.getNumber()}) tirou {i.getGrade()}")
            print("-"*60)
        elif option == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida")
main()
