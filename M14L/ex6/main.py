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
    print("6. Sair")

    return input("Escolha uma opção (1-6): ")

def main():
    college = College()

    while True:
        escolha = menu()
        
        if escolha == '1':
            nome = input("Digite o nome do aluno: ")
            student = Graduation(nome)
            college.add_student(student)
            print(f"Aluno {nome} adicionado com sucesso!")
        
        elif escolha == '2':
            nome = input("Digite o nome do aluno: ")
            student = Specialization(nome)
            college.add_student(student)
            print(f"Aluno {nome} adicionada com sucesso!")
        
        elif escolha == '3':
            nome = input("Digite o nome do aluno: ")
            student = Master(nome)
            college.add_student(student)
            print(f"Aluno {nome} adicionado com sucesso!")

        elif escolha == '4':
            nome = input("Digite o nome do aluno: ")
            student = Doctorate(nome)
            college.add_student(student)
            print(f"Aluno {nome} adicionado com sucesso!")
        
        elif escolha == '5':
            print("\nAlunos na faculdade:")
            college.list_students()
        
        elif escolha == '6':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")

if __name__ == '__main__':
    main()