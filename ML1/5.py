"""Fazer um programa que calcule e escreva o número de grãos de milho que podem ser
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha
o cuidado de testar se ele não sofre um overflow."""

def print_formatado(num):
     print("Número de grãos de milho: {:,}".format(num).replace(',', '.'))
    

def main():
    num_milho = 0
    for i in range(64):
        num_milho += 2 ** i
        
    print_formatado(num_milho)

main()