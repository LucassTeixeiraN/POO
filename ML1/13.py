# 13. A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os
# demais são dados pela soma dos dois anteriores. Faça um programa que imprima os
# “n” primeiros termos da série, sendo “n” dado pelo usuário.

def fibonacciCom(n):
    n1, n2 = 0, 1
    for _ in range(n - 1):
        n1, n2 = n2, n1 + n2
    return n1 if n == 0 else n2

def main():
    print("-" * 60)
    while True:
        try:
            numero = int(input("Insira um valor para saber qual número está nessa posição na sequência de Fibonacci: "))
            print(f'O número que ocupa a {numero}° posição é: {fibonacciCom(numero)}')
            print("-" * 60)
            break
        except ValueError:
            print("Número inválido. Tente novamente.")


main()
