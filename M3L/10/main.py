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
        opcao = int(input("Escolha uma das opções:\n1- Comparar a nota de dois alunos\n2- Colocar as notas dos alunos em ordem crescente\n3- sair\n"))
        return opcao
    except ValueError:
        print("Valor inválido")
        menu() 

def mapGrades(item):
    return item.grade

def mapNames(item):
    return item.name

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            students = []
            for i in range(2):
                name = input("Student name: ")
                grade = float(input("Student grade: "))
                students.append(Student(name,grade))

            if students[0].igualdade(students[1]):
                print("Os alunos tiraram a mesma nota")
            if students[0].maior(students[1]):
                print(f"O aluno {students[0].name} tirou a maior nota")
            if students[0].menor(students[1]):
                print(f"O aluno {students[1].name} tirou a maior nota")
        elif opcao == 2:
            print("Insira os alunos (insira 0 no nome quando não houver mais alunos)")
            students = []
            while True:
                name = input("Student name: ")
                if name == "0": 
                    break
                grade = float(input("Student grade: "))
                students.append(Student(name,grade))
            gradeList = list(map(mapGrades, students))
            random.shuffle(gradeList)
            newNameList = []
            for i in range(len(gradeList)):
                newNameList.append(0)
            gradeList.sort()
            
            for i in range(len(gradeList)):
                for j in students:
                    if j.checkGrade(gradeList[i]):
                        newNameList[i] = j.name
            print(gradeList)
            print(newNameList)
                        
            
            
        elif opcao == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida")



            
main()
