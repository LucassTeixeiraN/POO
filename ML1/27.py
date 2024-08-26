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

def precoMin(custo, copias):
    lucro = 1.2 * custo
    preco = lucro/copias

    return preco

def main():
    CUSTO_FIXO = 4397
    n_livros = 0
    while True:
        try:
            paginas = int(input("Insira o número de páginas do livro (insira 0 caso não haja mais livros)"))
            if paginas == 0:
                break
            n_livros += 1
            encadernacao = int(input("Insira o tipo de encadernação.\n1 - Simples\n2 - Especial\n3 - Luxo\n"))
            if encadernacao == 1:
                preco_enc = 4.3
            elif encadernacao == 2:
                preco_enc = 7.8
            else:
                preco_enc = 10.5

            copias = int(input("Insira o número de cópias previstas: "))

            if paginas > 0 and 1 <= encadernacao <= 3 and copias > 0:
                custoTotal = (paginas*0.03 + preco_enc)*copias + CUSTO_FIXO
main()

#OBS: Tenho q terminar
