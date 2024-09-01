"""Faça um programa que leia um conjunto de números positivos, sendo o conjunto
destes números finalizado quando for digitado um número negativo. Ao final, imprima
o maior e o menor número lido e a média deles."""

def numero_input():
    try:
        valor = float(input("Digite o número: "))
        return valor
    except:
        print("Número inválido. Digite novamente!")
        return numero_input()

def main():
    lista_positivos = []
    while True:
        num = numero_input()
        if num < 0:
            break
        
        lista_positivos.append(num)
        
    print(f'Conjunto de números: {lista_positivos}')
    print(f'Maior número: {max(lista_positivos)}')
    print(f'Menor número: {min(lista_positivos)}')
    print(f'Média dos números: {sum(lista_positivos) / len(lista_positivos)}')
    
main()