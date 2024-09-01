"""A convenção de graus Fahrenheit para Celsius é obtida pela fórmula C = 5. (F - 32)/9.
Escreva um programa que calcule e imprima uma tabela de graus centígrados em
função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes
simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5)."""

def FparaC(temperatura):
    return 5 * (temperatura - 32) / 9

def print_lista(lista: list[int]):
    for index, item in enumerate(lista, 1):
        if index % 5:
            print(f'{item:.2f}', end=' ')
        else:
            print(f'{item:.2f}')
        

def main():
    INICIO = 50
    FIM = 150
    PASSO = 5
    
    fahrenheit_lista = []
    for num in range(INICIO, FIM + 1, PASSO):
        fahrenheit_lista.append(FparaC(num))
    
    print_lista(fahrenheit_lista)

main()