# 15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série:
# 100/0! + 99/1! + 98/2! + 97/3!

def fatorial(N):
    if N == 0:
        return 1
    return N * fatorial(N-1)

def calcular_termos():
    soma = 0
    termo1 = 100
    termo2 = fatorial(0)

    for _ in range(10):
        soma += termo1 / termo2
        termo1 -= 1
        termo2 += 1

    return round(soma,2)
resultado = calcular_termos()
print("soma dos primeiros 10 termos é: ",resultado)
