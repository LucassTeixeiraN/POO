'''Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N
é fornecido pelo usuário.
Sabemos que:
N! = 1 x 2 x 3 x 4 x...x (N - 1) x N;
0! = 1, por definição.'''

def fatorial(N):
    if N == 0:
        return 1
    return N * fatorial(N-1)

def main():
    while True:
        try:
            N = int(input("Insira um valor para saber seu fatorial: "))
            if N < 0:
                print("Insira um numero nao negativo.")
                continue
            print(f"O fatorial de {N} é = {fatorial(N)}")
            break
        except (ValueError):
            print("Erro: valor inserido não é um número inteiro.")
main()