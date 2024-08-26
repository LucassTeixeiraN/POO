'''A multiplicação entre dois números inteiros pode ser definida como uma repetição da
adição de um deles. Exemplo: 3x4 = 4 + 4 + 4
Escreva uma função que multiplique dois números inteiros utilizando esse método. A
seguir, escreva um programa que peça ao usuário um número inteiro e imprima a
tabuada para aquele número (de 1 à 10) utilizando a função construída.'''

# Função para multiplicar dois números inteiros utilizando adição repetida
def multiplicacao(a, b):
    resp = f"{a}x{b} = "  # Inicia a string de resposta com a multiplicação

    for i in range(b):  # Loop para adicionar 'a' repetidamente 'b' vezes
        if a > 0:
            if i < b-1:
                resp += f"{a} + "  # Adiciona 'a' e um sinal de mais
            else:
                resp += f"{a} = {a*b}"  # Adiciona 'a' e o resultado final
        else:
            if i < b-1:
                resp += f"({a}) + "  # Adiciona 'a' entre parênteses e um sinal de mais
            else:
                resp += f"({a}) = {a*b}"  # Adiciona 'a' entre parênteses e o resultado final

    return resp  # Retorna a string de resposta

# Função principal para obter a entrada do usuário e imprimir a tabuada
def main():
    while True:
        try:
            print("-"*50)
            numero = int(input("Insira um número para ver sua tabuada: "))  # Solicita a entrada do usuário
            break
        except ValueError:
            print("Insira um número inteiro.")  # Mensagem de erro para entradas não inteiras

    print('-'*50)
    for i in range(1, 11):  # Loop para imprimir a tabuada de 1 a 10
        print(multiplicacao(numero, i))  # Chama a função de multiplicação e imprime o resultado
    print('-'*50)

# Chama a função principal se o script for executado diretamente
main()
