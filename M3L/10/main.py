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

def mapGrades(item):
    return item.grade

def main():
    while True:
        option = menu()
        if option == 1:
            students = []
            for i in range(2):
                name = input("Nome do estudante: ")
                grade = float(input("Nota do estudante: "))
                students.append(Student(name,grade))

            if students[0].equal(students[1]):
                print("Os alunos tiraram a mesma nota")
            if students[0].maior(students[1]):
                print(f"O aluno {students[0].name} tirou a maior nota")
            if students[0].menor(students[1]):
                print(f"O aluno {students[1].name} tirou a maior nota")
        elif option == 2:
            print("Insira os alunos (insira 0 no nome quando não houver mais alunos)")
            students = []
            while True:
                name = input("Student name: ")
                if name == "0": 
                    break
                grade = float(input("Student grade: "))
                students.append(Student(name,grade))
            #Coloca todas as notas dos Objects em uma lista e embaralha ela e logo em seguida coloca em ordem crescente
            gradeList = list(map(mapGrades, students))
            random.shuffle(gradeList)
            gradeList.sort()
            # cria uma lista e completa ela com 0s
            newNameList = []
            for i in range(len(gradeList)):
                newNameList.append(0)
            #Itera pela lista de notas procurando o aluno com essa nota, quando acha, coloca o nome desse aluno no mesmo índice da nota
            namesAlreadyUsed = []
            i = 0
            while i < len(gradeList):
                for j in students:
                    if j.checkGrade(gradeList[i]) and not j.name in namesAlreadyUsed:
                        newNameList[i] = j.name
                        namesAlreadyUsed.append(j.name)
                        i += 1
                        print(namesAlreadyUsed)

            for i in range(len(gradeList)):
                print(f"O aluno {newNameList[i]} tirou {gradeList[i]}")
    
        elif option == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida")



            
main()
