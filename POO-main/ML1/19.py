# Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
# a. A criança escolhe a tabuada a ser estudada.
# b. O programa gera um número aleatório e pergunta à criança qual o valor dele
# multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
# novamente, se acertar o programa pergunta à criança se ela deseja continuar
# respondendo.
# c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
# número de acertos e o número de erros cometidos pela criança.
import random

def verifConta(a, b):
    while True:
        try:
            resposta = int(input('Resposta: '))
            if a*b == resposta:
                return True
            return False
        except ValueError:
            print('Valor inválido.')

def gerarTabuada():
    tabuada = int(input("Qual tabuada de 1 a 10 você deseja estudar? "))
    n_aleatorio = random.randint(1, 11)

    
    return tabuada, n_aleatorio

def main():
    tabuada, n_aleatorio = gerarTabuada()
    acertos = erros = 0
    while True:
        try:
            print(f'{tabuada} x {n_aleatorio} = ?')

            if verifConta(tabuada, n_aleatorio):
                acertos += 1
                if input("Você acertou! Deseja continuar? [s/n] ").lower() == 's':
                    tabuada, n_aleatorio = gerarTabuada()
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
