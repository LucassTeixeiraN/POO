'''Elabore um outro programa didático nos mesmos moldes do anterior para treino da
divisão. Neste programa deve ser perguntado à criança o resultado da divisão e o
resto.'''

import random

def verifConta(a, b):
    while True:
        try:
            quociente = int(input('Quociente inteiro: '))
            resto = int(input('Resto: '))
            if a//b == quociente and a%b == resto:
                return True
            return False
        except ValueError:
            print('Valor inválido.')

def gerarDivis():
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)

    
    return n1, n2

def main():
    n1, n2 = gerarDivis()
    acertos = erros = 0
    while True:
        try:
            print('Qual é o quociente inteiro e o resto da seguinte divisão:')
            print(f'{n1} ÷ {n2}')

            if verifConta(n1, n2):
                acertos += 1
                if input("Você acertou! Deseja continuar? [s/n] ").lower() == 's':
                    n1, n2 = gerarDivis()
                    continue
                else:
                    print("-"*60)
                    print(f"{acertos + erros} perguntas foram respondidas")
                    print(f"{acertos} acertos")
                    print(f"{erros} erros")
                    print("-"*60)
                    break
            else:
                erros += 1
                print("Tente novamente")
                continue


        except ValueError:
            print("Valor inválido.")

main()
