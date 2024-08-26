'''Elabore um programa que:
• Mostre um menu de opções de conversão entre moedas (1 – dólar americano,
2 – euro, 3 – libra esterlina e 4 – yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.

Moeda Valor              (R$)
Dólar americano          3,258
Euro                     4,095
Libra esterlina          4,529
Yuan                     0,515'''


def conversor(real, conversao, moeda):
    return f"{real:.2f}R$ = {(real*conversao):.2f} {moeda}"

    
def menu():
    print("-"*60)
    print("Para qual moeda você deseja converter o valor em reais?")
    print("\n1 - Dólar americano\n2 - Euro\n3 - Libra esterlina\n4 - Yuan\n5 - Sair do Programa")
    print("-"*60)
    while True:
        try:
            escolha = int(input("Insira a opção desejada: "))
            return escolha
        except ValueError:
            print("Valor inválido")
            

def main():
    MOEDAS = ("Dólares Americanos", "Euros", "Libras Esterlinas", "Yuan")
    CONVERSOES = (3.258, 4.095, 4.529, 0.515)
    
    while True:
        escolha = menu()
        try:
            if 1 <= escolha <= 4:
                valor = float(input("Insira o valor a ser convertido em reais:\n"))
                print(conversor(valor, CONVERSOES[escolha-1], MOEDAS[escolha-1]))
                print("-"*60)
            elif escolha == 5:
                print("Saindo do programa")
                print("-"*60)
                break
            else:
                print("Insira uma opção válida")
                print("-"*60)
        except ValueError:
            print("Valor inválido")
            print("-"*60)
    
    
main()