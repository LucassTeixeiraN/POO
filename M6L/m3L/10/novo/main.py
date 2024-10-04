# 10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
# Student. Um método deve testar a igualdade. Um segundo método deve testar para
# menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
# método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
# função main que testa todos os operadores de comparação. Em seguida, coloque
# vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
# com esta lista e exiba todas as informações dos alunos.

from student import Student
from schoolClass import SchoolClass

def menu():
    try:
        option = int(input("Escolha uma das opções:\n1- Comparar a nota de dois alunos\n2- Colocar as notas dos alunos em ordem crescente\n3- sair\n"))
        return option
    except ValueError:
        print("Valor inválido")
        menu() 

def errorMessage():
    print("Valor inválido")

def newStudent(num):
    try:
        name = input(f"Nome do {num}° estudante: ")
        number = int(input(f"Número do {num}° estudante: "))
        grade = float(input(f"Nota do {num}° estudante: "))
        if grade >= 0 and grade <= 10:
            return Student(name, grade, number)
    except ValueError:
        errorMessage()
        newStudent()

def compareTwoStudents():
    student1 = newStudent(1)           
    student2 = newStudent(2)           

    myClass = schoolClass([student1, student2])
    myClass.compareStudents(myClass.getStudents()[0], myClass.getStudents()[1])

def studentsInOrder():
    studentsNum = int(input("Insira o número de alunos da turma: "))
    students = []
    for i in range(studentsNum):
        students.append(newStudent(i+1))
    myClass = schoolClass(students)
    print("-"*60)
    myClass.__str__()

def main():
    while True:
        option = menu()
        if option == 1:
            compareTwoStudents()
        elif option == 2:
            studentsInOrder()
        elif option == 3:
            print("Finalizando programa")
            break
        else:
            print("Opção inválida")
main()
