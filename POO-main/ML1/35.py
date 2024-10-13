'''Faça um programa que apresente na tela um menu com as seguintes opções: 1.
Converter um ângulo em graus para radiano; 2. Calcular o seno de um ângulo, 3.
Calcular o valor de . 4. Resolver uma equação do segundo grau; 0. Sair. Depois de
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já
implementou.'''

def fatorial(N):
    if N == 0:
        return 1
    return N * fatorial(N-1)

def graus_para_radiano(graus):
    rad = (graus * calculo_pi())/180
    return rad

def calculo_seno(angulo_rad):
    sen = 0
    sinal = 1
    for i in range(10):
        sen += ((angulo_rad**(2*i+1)) / fatorial(2*i+1)) * sinal
        sinal *= -1
            
    return sen

def calculo_pi():
    pi = 0
    sinal = 1
    divisor = 1
    for i in range(1, 1_000_000):
        pi += (4 / divisor) * sinal
        sinal *= -1
        divisor += 2
    return pi

def equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "A equação não tem raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        return f"A equação tem uma raiz real: x = {x}"
    else:
        raiz_delta = delta ** (1/2)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        return f"A equação tem duas raízes reais: x1 = {x1} e x2 = {x2}"

def main():
    opcao = -1
    while opcao != 0:
        print("\nMenu:")
        print("1. Converter um ângulo em graus para radiano")
        print("2. Calcular o seno de um ângulo")
        print("3. Calcular o valor de π")
        print("4. Resolver uma equação do segundo grau")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))
        
        match(opcao):
            case 1:
                graus = float(input("Digite o ângulo em graus: "))
                radianos = graus_para_radiano(graus)
                
                print(f"{graus} graus são {radianos:.4f} radianos.")
            case 2:
                angulo = float(input("Digite o ângulo em graus: "))
                angulo_rad = graus_para_radiano(angulo)
                seno = calculo_seno(angulo_rad)
                
                print(f"O seno de {angulo} graus é {seno:.4f}.")
            case 3:
                pi = calculo_pi()
                print(f"O valor de π é {pi:.4f}.")
            case 4:
                a = float(input("Digite o coeficiente a: "))
                b = float(input("Digite o coeficiente b: "))
                c = float(input("Digite o coeficiente c: "))
                
                resultado = equacao_segundo_grau(a, b, c)
                print(resultado)
            case 0:
                print('Fechando o programa...')
            case _:
                print("Opção inválida. Tente novamente.")
                

main()
