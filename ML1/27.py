'''O custo de produção de um livro é constituído dos custos por página, mais o custo
de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o
custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo
utilizada a seguinte tabela:
• Encadernação simples: R$4,30
• Encadernação especial: R$7,80
• Encadernação luxo: R$10,50
Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de
encadernação e o número de vendas previstas (número de cópias) e:
a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e
o preço de venda para que a editora tenha um lucro de 20%.
b. Imprima o total de livros analisados.
c. Imprima o preço médio de venda dos livros (com lucro de 20%).
d. Imprima o preço de venda dos livros mais barato e mais caro.'''

# Define o tipo de encadernação
#OBS: Tirei da main pq achei q ia ocupar muito espaço
def tipoEncad():
    while True:
        tipo = int(input("Insira o tipo de encadernação.\n1 - Simples\n2 - Especial\n3 - Luxo\n"))
        if tipo == 1:
            return 4.3
        elif tipo == 2:
            return 7.8
        elif tipo == 3:
            return 10.5
        else:
            print("Tipo de encadernação inválido.")
            print("-"*60)

# Calcula o preço do livro para que se tenha 20% de lucro
def precoMin(custo, copias):
    vendas = 1.2*custo
    preco = vendas/copias
    return preco

def precoMedio(preco, n):
    preco_soma = 0
    for i in preco:
        preco_soma += i
    
    return preco_soma/n

def maisBarato(precos):
    mais_barato = precos[0]

    for i in precos:
        if i < mais_barato:
            mais_barato = i

    return mais_barato

def maisCaro(precos):
    mais_caro = precos[0]

    for i in precos:
        if i > mais_caro:
            mais_caro = i
    return mais_caro


def main():
    CUSTO_FIXO = 4397
    n_livros = 0
    precos = []
    while True:
        try:
            print("-"*60)
            paginas = int(input("Insira o número de páginas do livro (insira 0 caso não haja mais livros)"))
            if paginas == 0:
                break

            preco_enc = tipoEncad()

            copias = int(input("Insira o número de cópias previstas: "))
            
            n_livros += 1

            if paginas > 0 and copias > 0:
                custo_total = (paginas*0.03 + preco_enc)*copias + CUSTO_FIXO
                custo_minimo = precoMin(custo_total, copias)
                print(f"\nO preço do livro pra que se tenha um lucro de 20% é de R${custo_minimo:.2f}.")
                precos.append(custo_minimo)

        except ValueError:
            print("valor inválido")
    
    print("-"*60)
    print(f"{n_livros} foram analisados.")
    print(f"O preço médio de venda foi de R${precoMedio(precos, n_livros):.2f}.")
    print(f"O livro mais barato é vendido por R${maisBarato(precos):.2f}.")
    print(f"O livro mais caro é vendido por R${maisCaro(precos):.2f}.")
main()
