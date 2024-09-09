# 14. Construa um programa que calcule e mostre a soma dos 30 primeiros termos da
# série:
# 450/10 + 445/11 + 440/12 + 435/13 + ... 

def calcular_soma_serie():
    soma = 0
    termo1 = 450
    termo2 = 10

    for i in range(30):
        soma += termo1 / termo2
        termo1 -= 5
        termo2 += 1

    return round(soma,2)

resultado = calcular_soma_serie()
print("A soma dos 30 primeiros termos da série é:", resultado)

