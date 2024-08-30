'''O seno de um ângulo em radianos, no intervalo de 0 à pi/2
pode ser calculado através

da série de McLaurin, apresentada a seguir:


sen x = x/1! - x³/3! + x**5/5! - ....



a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (180° = pi rad)

b. Escreva uma função que receba como parâmetro um ângulo em graus, a
precisão requerida para o cálculo e retorne o seu seno, utilizando a função de
conversão graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno.'''
    
pi = 3.14
def a(graus):
    rad = (graus * pi)/180
    return rad

def fatorial(N):
    if N == 0:
        return 1
    return N * fatorial(N-1)

def seno(graus, precisao):
    rad = a(graus)
    sen = 0
    sinal = 1
    for i in range(precisao):
        if sinal == 1:
            sen += (rad**(2*i+1)) / fatorial(2*i+1)
        else:
            sen -= (rad**(2*i+1)) / fatorial(2*i+1)
        sinal *= -1
            
    return sen

def menu():
    print("-"*30, "MENU", "-"*30)
    print("\n1- Converter ângulo em graus para radianos\n2- Calcular o seno de um ângulo em graus\n3- Sair do programa")
    opcao = int(input("\nInsira a opção desejada: "))
    if opcao < 1 or opcao > 3:
        print("\nErro: Selecione uma opção válida.")
    return opcao
        
def main():
    while True:
        x = input("Aperte ENTER para ir ao menu.")
        if x == '':    
            try:
                opcao = menu()
                if opcao == 1:
                    graus = float(input("Insira um ângulo em graus: "))
                    rad = a(graus)
                    print(f"O ângulo {graus}° é = {rad:.2f} radianos.")
                elif opcao == 2:
                    graus = float(input("Insira um ângulo em graus: "))
                    precisao = int(input("Insira a precisão desejada: "))
                    z = seno(graus, precisao)
                    print(f"O seno de {graus}° na precisão {precisao} é = {z:.2f}.")
                elif opcao == 3:
                    print("Saindo do programa.")
                    break
            except(ValueError, OverflowError):
                print("Erro: Dados inválidos.")
            
main()