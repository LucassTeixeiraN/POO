'''Escreva as seguintes funções:
a. CparaF – faz a conversão de uma temperatura em graus C para graus F.
b. CparaK – faz a conversão de uma temperatura em C para Kelvin (C=K-273)
c. KparaC – faz a conversão de K para C.
d. KparaF – faz a conversão de K para F (dica: utilize as funções anteriores)
e. FparaK – faz a conversão de F para K.
A seguir, faça um programa que apresente continuamente um menu na tela com
todas as opções de conversão que você implementou. Uma vez feita a opção, o
programa lê do teclado o valor a ser convertido e imprime o resultado.'''
def cParaF(C):
    F = (C * 9/5) + 32
    return F
def cParaK(C):
    K = C + 273
    return K
def kParaC(K):
    C = K - 273
    return C
def kParaF(K):
    F = cParaF(kParaC(K))
    return F
def fParaK(F):
    K = (5/9*(F - 32)) + 273
    return K

def menu():
        print("-"*30, "MENU", "-"*30)              
        print('''
        1- C° para F°                   4- K° para F°
        2- C° para K°                   5- F° para K°
        3- K° para C°                   6- SAIR
              ''')
        opcao = int(input("Insira a opção desejada: "))
        return opcao

def main():
    while True:
        x = input("APERTE ENTER PARA IR AO MENU\n")
        if x == '':
            opcao = menu()
            if opcao == 1:
                C = float(input("Digite o valor a ser convertido: "))
                F = cParaF(C)
                print(f"{C}C° = {F:.2f}F°")
                continue       
            elif opcao == 2:
                C = float(input("Digite o valor a ser convertido: "))
                K = cParaK(C)
                print(f"{C}C° = {K:.2f}K°")
                continue
            elif opcao == 3:
                K = float(input("Digite o valor a ser convertido: "))
                C = kParaC(K)
                print(f"{K}K° = {C:.2f}C°")
                continue
            elif opcao == 4:
                K = float(input("Digite o valor a ser convertido: "))
                F = kParaF(K)
                print(f"{K}K° = {F:.2f}F°")
                continue
            elif opcao == 5:
                F = float(input("Digite o valor a ser convertido: "))
                K = fParaK(F)
                print(f"{F}F° = {K:.2f}K°")
                continue
            elif opcao == 6:
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida.\n")
                continue
main()