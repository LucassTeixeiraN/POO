"""Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são
fornecidos os seguintes dados:
• O preço o kWh
• O número de identificação de cada consumidor
• A quantidade de kWh consumido no mês por cada um
• O código do tipo de consumidor (residencial, comercial ou industrial)

A partir desses dados calcule:
a. Para cada consumidor, o total a pagar;
b. O maior consumo verificado;
c. O menor consumo verificado;
d. O total de consumo (em kWh) para cada um dos três tipos de consumidores
e. A média de consumo (em kWh) para cada um dos três tipos de consumidores
f. O total arrecadado pela companhia elétrica."""

def input_usuario():
    valor_kwh = float(input("Digite o preço do kWh: "))
    
    continuar = 'S'
    consumidores = []
    while continuar == 'S':
        num_identificacao = input("Digite o número de identificação: ")
        quantidade_consumida = float(input("Digite a quantidade de kWh consumida no mês: "))
        codigo_consumidor = input("Digite o código (residencial, comercial ou industrial): ")
        
        consumidores.append({
            'numero': num_identificacao,
            'quantidade': quantidade_consumida,
            'valor': quantidade_consumida * valor_kwh,
            'codigo': codigo_consumidor
        })
        
        continuar = input("Deseja continuar? (S/N)").upper().strip()

    return consumidores

def main():
    
    consumidores = input_usuario()
    consumidor_maior_consumo = max(consumidores, key=lambda x: x['quantidade'])
    consumidor_menor_consumo = min(consumidores, key=lambda x: x['quantidade'])
    total, qtd_consumidores = {}, {}
    
    for consumidor in consumidores:
        codigo = consumidor['codigo']
        valor = consumidor['valor']
        
        #Inicializa o código, caso ele não tenha sido adicionado anteriormente
        if codigo not in total:
            total[codigo] = 0
            qtd_consumidores[codigo] = 0
        
        total[codigo] += valor
        qtd_consumidores[codigo] += 1
        
        print(f"Total a pagar pelo consumidor {consumidor['numero']}: {consumidor['valor']}")
        
    print(f"\nO consumidor {consumidor_maior_consumo['numero']} foi verificado com o maior consumo, sendo de: {consumidor_maior_consumo['valor']}")
    print(f"O consumidor {consumidor_menor_consumo['numero']} foi verificado com o menor consumo, sendo de: {consumidor_menor_consumo['valor']}\n")
    for key in ['residencial', 'comercial', 'industrial']:
        if key in total:
            print(f'O total de consumo pelo código {key} foi: {total[key]}')
            print(f'A média de consumo pelo código {key} foi: {total[key] / qtd_consumidores[key]}\n')
    print('Total arrecadado pela companhia elétrica: ', sum(total.values()))

main()