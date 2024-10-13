'''Faça um programa didático para estudo das raízes quadradas dos números, da
seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta
qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as
mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma
semelhante aos anteriores.'''
import random
def numAleat():
    return random.randint(1, 100)

def calcQuadrad(numero):
    return numero ** 2

def perguntRaiz(quadrado):
    resposta = input(f"Qual é a raiz quadrada de {quadrado}? \n")
    try:
        resposta = int(resposta)
    except ValueError:
        print("Erro! Por favor, digite um número.")
        return perguntRaiz(quadrado)
    return resposta

def verifResp(resposta, numero_aleatorio):
    return resposta == numero_aleatorio

def msgERRO(numero_aleatorio, quadrado):
    print(f"Erro! A raiz quadrada de {quadrado} é {numero_aleatorio}. Continue tentando!")

def atualizarEstat(perguntas, acertos, erros):
    perguntas += 1
    print(f"Perguntas: {perguntas} / Acertos: {acertos} / Erros: {erros}")
    return perguntas

def main():
    perguntas = 0
    acertos = 0
    erros = 0

    while True:
        numero_aleatorio = numAleat()
        quadrado = calcQuadrad(numero_aleatorio)

        resposta = perguntRaiz(quadrado)
        if verifResp(resposta, numero_aleatorio):
            print("Parabéns! Você acertou!")
            acertos += 1
        else:
            msgERRO(numero_aleatorio, quadrado)
            erros += 1

        perguntas = atualizarEstat(perguntas, acertos, erros)

        resposta_continuar = input("Deseja continuar? (s/n): ")
        if resposta_continuar.lower() != 's':
            break

    print("Obrigado por estudar comigo! Saindo do programa.")

main()

