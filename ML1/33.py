'''O valor aproximado de  pode ser calculado a partir da série:
Escreva uma função que calcule o valor de , com precisão dada como parâmetro.'''

def calculo_pi(precisao):
  pi = 0
  sinal = 1
  divisor = 1
  for i in range(1, precisao + 1):
    pi += (4 / divisor) * sinal
    sinal *= -1
    divisor += 2
  return pi

def main():
  precisao_pi = int(input('Digite a precisão desejada para o cálculo de π: '))
  valor_pi = calculo_pi(precisao_pi)

  print(f'O valor de π com precisão de {precisao_pi} termos é {valor_pi}')

main()