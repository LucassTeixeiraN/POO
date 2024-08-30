'''Uma equação do segundo grau é escrita
ax**2 + bx + c = 0
e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva
uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.'''


# Função para resolver a equação do segundo grau
def equacao(a, b, c):
    delta = b**2 - 4*a*c  # Calcula o discriminante (delta)

    if delta > 0:
        raiz1 = (-b + delta**0.5) / (2*a)  # Calcula a primeira raiz
        raiz2 = (-b - delta**0.5) / (2*a)  # Calcula a segunda raiz
        print(f"A equação tem duas raízes reais:")
        print(f"Raiz 1 (x1) = {raiz1}")
        print(f"Raiz 2 (x2) = {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)  # Calcula a raiz dupla
        print(f"A equação tem uma raiz real (raiz dupla):")
        print(f"Raiz (x) = {raiz}")
    else:
        print("A equação não tem raízes reais.")  # Caso delta seja negativo

# Função principal para obter a entrada do usuário e resolver a equação
def main():
    try:
        a = float(input("Informe o valor de a: "))  # Solicita o valor de a
        b = float(input("Informe o valor de b: "))  # Solicita o valor de b
        c = float(input("Informe o valor de c: "))  # Solicita o valor de c
    except ValueError:
        print("Valores inválidos")  # Mensagem de erro para entradas não numéricas

    equacao(a, b, c)  # Chama a função para resolver a equação

# Chama a função principal se o script for executado diretamente
main()
