# 16. Sendo
# S

# N
# = 1− + − + − +
# 1
# 2
# 1
# 3
# 1
# 4
# 1
# 5
# 1
# ... , construa um programa que leia N, calcule e mostre

# o valor da série S.


def calcular_serie(N):
    S = 0
    for i in range(1, N + 1):
        S += (-1)**(i + 1) / i
    return S




def main():
    while True:
        try:
            N = int(input("Insira um número para conseguir o resultado da sequência até ele: "))
            resultado = calcular_serie(N)
            print(f"O valor da série S para N = {N} é:  {resultado:2f}")
           
            break
        except ValueError:
            print("Valor inválido! Tente novamente.")

main()

