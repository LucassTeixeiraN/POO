# 17. O número  pode ser calculado através da série: ...
# 9
# 4
# 7
# 4
# 5
# 4
# 3
# 4
#  = 4 − + − + − Faça um
# programa para calcular o valor de  com precisão de 0,00001 (o programa encerra
# quando a parcela da série for menor que a precisão).


def calcular_pi(precisao):
    pi = 0
    termo = 1
    i = 0
    while abs(termo) > precisao:
        termo = 4 * (-1)**i / (2 * i + 1)
        pi += termo
        i += 1
    return round(abs(pi),4)

precisao = 0.0001
valor_pi = calcular_pi(precisao)
print(f'O valor de π calculado é: {valor_pi}')

