'''Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário
aos expectadores, no qual constava a idade e a sua opinião em relação ao filme,
segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo
estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule
e imprima:
a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo.
b. A percentagem de ótimo, bom, regular, ruim e péssimo.
c. A idade do mais velho entrevistado.
d. A idade do mais novo entrevistado.'''
CAPACIDADE = 50

def ler_dados():
    respostas = {"ótimo": 0, "bom": 0, "regular": 0, "ruim": 0, "péssimo": 0}
    idades = []
    opiniao_map = {1: "ótimo", 2: "bom", 3: "regular", 4: "ruim", 5: "péssimo"}
    for i in range(CAPACIDADE):
        while True:
            try:
                idade = int(input(f"\nDigite a idade do espectador {i+1}: "))
                if idade < 0:
                    print("Erro: Idade deve ser um numero positivo")
                    continue
                break
            except ValueError:
                print("Erro: idade deve ser um número inteiro")
        while True:
            try:
                opiniao = int(input(f"\nDigite a opinião do espectador {i+1}\n1- ótimo\n2- bom\n3- regular\n4- ruim\n5- péssimo \n"))
                escolha = opiniao_map.get(opiniao, "ERRO")
                if escolha != "ERRO":
                    break
                print("Erro: opinião inválida")
            except(ValueError):
                print("Erro: Opiniao invalida")
        respostas[escolha] += 1
        idades.append(idade)
    return respostas, idades

def calcular_percentagens(respostas):
    total = sum(respostas.values())
    return {k: (v / total) * 100 for k, v in respostas.items()}

def encontrar_idades_extremas(idades):
    return max(idades), min(idades)

def imprimir_resultados(respostas, percentagens, idade_mais_velha, idade_mais_nova):
    print("-"* 30, "\nQuantidade de respostas:")
    for k, v in respostas.items():
        print(f"{k}: {v}")
    print("-"*30)
    print("Porcentagens:")
    for k, v in percentagens.items():
        print(f"{k}: {v:.2f}%")
    print("-"*30)
    print("Idades extremas:")
    print(f"Mais velho: {idade_mais_velha}")
    print(f"Mais novo: {idade_mais_nova}")
    print("-"*30)

def main():
    print("-"*30,"Bem-vindo ao programa de avaliação de filmes!","-"*30)
    respostas, idades = ler_dados()
    percentagens = calcular_percentagens(respostas)
    idade_mais_velha, idade_mais_nova = encontrar_idades_extremas(idades)
    imprimir_resultados(respostas, percentagens, idade_mais_velha, idade_mais_nova)

main()