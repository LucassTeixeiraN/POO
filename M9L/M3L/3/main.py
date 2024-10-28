'''Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''
from account import Account
from customer import Customer

def input_verificado(input_string, tipo):
    try:
        valor = tipo(input(input_string))
        return valor
    except ValueError:
        print("Número inválido. Digite novamente!")
        return input_verificado(input_string, tipo)

def main():
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = Customer(nome_cliente)
    
    saldo = input_verificado("Digite o saldo inicial da conta: ", float)
    conta = Account(saldo)
    cliente.add_account(conta)
    print("Conta criada com sucesso!")

    while True:
        print("\nMenu:")
        print("1. Ver saldo da conta")
        print("2. Debitar da conta")
        print("3. Sair")
        
        opcao = input_verificado("Escolha uma opção: ", int)
        print()
        
        if opcao == 1:
            print(conta)
        
        elif opcao == 2:
            quantidade = input_verificado("Digite a quantidade a ser debitada da conta: ", float)
            conta.debit(quantidade)
        
        elif opcao == 3:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()