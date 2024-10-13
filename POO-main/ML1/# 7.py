# 7. Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
# número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
# quantidade vendida. A partir desses dados imprima: o número total de mercadorias
# diferentes lidas, o faturamento total e o lucro total do armazém.

def calcular_balanco(mercadorias):
    faturamento_total = 0
    lucro_total = 0
    total_mercadorias = len(mercadorias)
    for i in mercadorias:
        faturamento_total += i['preco_venda'] * i['quantidade_vendida']
        lucro_total += (i['preco_venda'] - i['preco_custo']) * i['quantidade_vendida']
    
    return (total_mercadorias, faturamento_total, lucro_total)
    
def coletarMercadoria():
    mercadorias = []
    
    while True:
        try:
            nome = input("Digite o nome da mercadoria (ou 'sair' para finalizar): ")
            if nome.lower() == 'sair':
                break
            preco_custo = float(input(f"Digite o preço de custo de {nome}: "))
            preco_venda = float(input(f"Digite o preço de venda de {nome}: "))
            quantidade_vendida = int(input(f"Digite a quantidade vendida de {nome}: "))
            
            mercadoria = {
                'nome': nome,
                'preco_custo': preco_custo,
                'preco_venda': preco_venda,
                'quantidade_vendida': quantidade_vendida
            }
            mercadorias.append(mercadoria)
        except ValueError:
            print("Valores inválidos")
    return mercadorias

def main():
    mercadoria = coletarMercadoria()
    print(f"\nNúmero total de mercadorias diferentes: {calcular_balanco(mercadoria)[0]}")
    print(f"Faturamento total: R$ {calcular_balanco(mercadoria)[1]:.2f}")
    print(f"Lucro total: R$ {calcular_balanco(mercadoria)[2]:.2f}")
main()
