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

def max_lista(lista):
    maior = 0
    for item in lista:
        if item > maior:
            maior = item
    return maior

def min_lista(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

def media_lista(lista):
    tamanho = soma = 0
    for item in lista:
        soma += item
        tamanho += 1
    return soma / tamanho

def main():
    lista_positivos = []
    while True:
        num = numero_input()
        if num < 0:
            break
        
        lista_positivos.append(num)
    
    if lista_positivos:
        print(f'Conjunto de números: {lista_positivos}')
        print(f'Maior número: {max_lista(lista_positivos)}')
        print(f'Menor número: {min_lista(lista_positivos)}')
        print(f'Média dos números: {media_lista(lista_positivos)}')
    else:
        print(f'O conjunto está vazio.')
    
main()
