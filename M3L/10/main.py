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
    grade = float(input(f"Nota do {num}° estudante: "))
    return Student(name,grade)

def compareStudents(student1, student2):
    if student1.__eq__(student2):
        print("Os alunos tiraram a mesma nota")
    if student1.__gt__(student2):
        print(f"O aluno {student1.getName()} tirou a maior nota")
    if student1.__lt__(student2):
        print(f"O aluno {student2.getName()} tirou a maior nota")

def mapGrades(item):
    return item.grade

#Coloca todas as notas dos Objects em uma lista e embaralha ela e logo em seguida coloca em ordem crescente
def listGrades(list):
    gradeList = list(map(mapGrades, list))
    random.shuffle(gradeList)
    gradeList.sort()
    return gradeList

def indexMatch(gradeList, studentList):
    # cria uma lista e completa ela com 0s
    nameList = []
    for i in range(len(gradeList)):
        nameList.append(0)

    #Itera pela lista de notas procurando o aluno com essa nota, quando acha, coloca o nome desse aluno no mesmo índice da nota
    namesAlreadyUsed = []
    i = 0
    while i < len(gradeList):
        for j in studentList:
            if j.checkGrade(gradeList[i]) and not j.name in namesAlreadyUsed:
                nameList[i] = j.name
                namesAlreadyUsed.append(j.name)
                i += 1
    
    return nameList

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

            gradesList = listGrades(students)

            nameList = indexMatch(gradesList, students)

            for i in range(len(gradesList)):
                print(f"O aluno {nameList[i]} tirou {gradesList[i]}")
    
        elif option == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida")

main()
