'''Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''
from account import Account, premium_debit, regular_debit

def inputVerificado(input_string, type):
    try:
        valor = type(input(input_string))
        return valor
    except:
        print("Número inválido. Digite novamente!")
        return inputVerificado(input_string, type)

def main():
    saldo = inputVerificado("Digite o saldo inicial da conta: ", float)
    conta = Account(saldo)
    print("Conta criada com sucesso!")

    while True:
        print("\nMenu:")
        print("1. Ver saldo da conta")
        print("2. Debitar da conta")
        print('3. Débito premium')
        print("4. Sair")
        
        opcao = inputVerificado("Escolha uma opção: ", int)
        print()
        
        if opcao == 1:
            print(conta)
        
        elif opcao == 2:
            quantidade = inputVerificado("Digite a quantidade a ser debitada da conta: ", float)
            conta.debit(quantidade, regular_debit)
        
        elif opcao == 3:
            quantidade = inputVerificado("Digite a quantidade a ser debitada da conta: ", float)
            conta.debit(quantidade, premium_debit)
        
        elif opcao == 4:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()
