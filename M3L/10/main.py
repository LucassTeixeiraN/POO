from student import Student

def menu():
    try:
        opcao = int(input("Escolha uma das opções:\n1- Comparar a nota de dois alunos\n2- Colocar as notas dos alunos em ordem crescente\n3- sair"))
        if opcao < 1 and opcao > 3:
            raise Exception
        else:
            return opcao
    except ValueError:
        print("Valor inválido")
        menu() 

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


            
main()