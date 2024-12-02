'''Implemente um sistema de Gestão Acadêmica com os tipos de estudante (graduação,
especialização, mestrado, doutorado, etc.), evidenciando a classe Student como uma
classe abstrata.'''
from students import Graduation, Specialization, Master, Doctorate
from college import College

def menu():
    print("\n===== Menu =====")
    print("1. Adicionar aluno em graduação")
    print("2. Adicionar aluno em especialização")
    print("3. Adicionar aluno fazendo mestrado")
    print("4. Adicionar aluno fazendo doutorado")
    print("5. Listar alunos")
    print("6. Fazer aluno estudar")
    print("7. Sair")

    return input("Escolha uma opção (1-7): ")

def main():
    college = College()

    while True:
        escolha = menu()
        
        if escolha == '1':
            nome = input("Digite o nome do aluno: ")
            student = Graduation(nome)
            college.add_student(student)
        
        elif escolha == '2':
            nome = input("Digite o nome do aluno: ")
            student = Specialization(nome)
            college.add_student(student)
        
        elif escolha == '3':
            nome = input("Digite o nome do aluno: ")
            student = Master(nome)
            college.add_student(student)

        elif escolha == '4':
            nome = input("Digite o nome do aluno: ")
            student = Doctorate(nome)
            college.add_student(student)
        
        elif escolha == '5':
            print("\nAlunos na faculdade:")
            college.list_students()

        elif escolha == '6':
            print("\n===== Alunos para Estudo =====")
            for i, student in enumerate(college.students, start=1):
                print(f"{i}. {student}")
            idx = int(input("Escolha o número do aluno para estudar: ")) - 1
            if 0 <= idx < len(college.students):
                college.students[idx].estudar()
            else:
                print("Opção inválida.")
        
        elif escolha == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")

if __name__ == '__main__':
    main()
