'''Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''
from account import Account

def inputVerificado(input_string):
    try:
        valor = float(input(input_string))
        return valor
    except:
        print("Número inválido. Digite novamente!")
        return inputVerificado(input_string)

def main():
    saldo = inputVerificado("Digite o saldo da conta: ")
    conta = Account(saldo)

    print("O saldo foi inserido \n")
    print("Digite um número negativo para sair")
    while True:
        debito = inputVerificado("Digite o valor a debitar: ")
        if debito < 0:
            break

        conta.debit(debito)

main()