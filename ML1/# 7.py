# 7. Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
# número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
# quantidade vendida. A partir desses dados imprima: o número total de mercadorias
# diferentes lidas, o faturamento total e o lucro total do armazém.

def calcular_balanco():

    mercadorias = []
    
    while True:
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
    
    total_mercadorias = len(mercadorias)
    faturamento_total = sum(m['preco_venda'] * m['quantidade_vendida'] for m in mercadorias)
    lucro_total = sum((m['preco_venda'] - m['preco_custo']) * m['quantidade_vendida'] for m in mercadorias)
    
    print(f"\nNúmero total de mercadorias diferentes: {total_mercadorias}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

# Chama a função para executar o programa
calcular_balanco()
 # colocar mais funções 
