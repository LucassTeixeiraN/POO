from employee import Employee, aumento_percentual, aumento_fixo

def menu():
    print("\nMenu:")
    print("1. Mostrar Empregado")
    print("2. Aplicar Aumento de Salário")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    nome = input("Digite o nome do empregado: ")
    sobrenome = input("Digite o sobrenome do empregado: ")
    salario = float(input("Digite o salário do empregado: "))
    empregado = Employee(nome, sobrenome, salario)
    
    while True:
        escolha = menu()
        
        if escolha == '1':
            print(empregado)
        
        elif escolha == '2':
            tipo_aumento = input("Escolha o tipo de aumento (percentual/fixo): ").strip().lower()
            if tipo_aumento == 'percentual':
                percentual = float(input("Digite o percentual de aumento: "))
                empregado.setAumentoSalario(aumento_percentual, percentual)
                print("Aumento aplicado com sucesso!")
            elif tipo_aumento == 'fixo':
                valor = float(input("Digite o valor do aumento: "))
                empregado.setAumentoSalario(aumento_fixo, valor)
                print("Aumento aplicado com sucesso!")
            else:
                print("Tipo de aumento inválido.")
        
        elif escolha == '3':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
