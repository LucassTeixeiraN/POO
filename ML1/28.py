'''
Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:
Tipo Quantidade vendida Comissões
8 K 10 ou mais R$ 550 por TV vendida
Menos que 10 R$ 350 por TV vendida
4 K 10 ou mais R$ 420 por TV vendida
Menos que 10 R$ 250 por TV vendida
7
Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de
5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
com os descontos). Além disso, no final, o programa deve:
a. Imprimir o número de funcionários.
b. Imprimir o total de salários pagos.
c. Imprimir a média das comissões.
d. Imprimir o valor da maior e da menor comissão paga pelo departamento. '''

def calcula_comissao(qtd_4k, qtd_8k):
    comissao_4k = qtd_4k * (420 if qtd_4k >= 10 else 250)
    comissao_8k = qtd_8k * (550 if qtd_8k >= 10 else 350)

    return comissao_4k, comissao_8k

def calcula_salario_liquido(salario_bruto, comissao_4k, comissao_8k):
    salario_com_comissao = salario_bruto + comissao_4k + comissao_8k
    salario_liquido = 0.92 * salario_com_comissao
    if salario_liquido > 950:
        salario_liquido *= 0.95
    return salario_liquido

def main():
    qtd_funcionarios = 0
    salario_total = 0
    comissao_lista = []

    while True:
        salario_bruto = float(input('Qual o salário do funcionário? '))
        qtd_4k = int(input('Quantidade de TVs 4K vendidas: '))
        qtd_8k = int(input('Quantidade de TVs 8K vendidas: '))
        
        comissao_4k, comissao_8k = calcula_comissao(qtd_4k, qtd_8k)
        salario_liquido = calcula_salario_liquido(salario_bruto, comissao_4k, comissao_8k)
        print('Salário líquido: ', salario_liquido)

        qtd_funcionarios += 1
        salario_total += salario_bruto + comissao_4k + comissao_8k
        
        comissao_lista.extend([comissao_4k, comissao_8k])

        if input('Deseja inserir mais funcionários? (S/N) ').strip().upper() == 'N':
            break

    print('-' * 30)
    print('Número de funcionários: ', qtd_funcionarios)
    print('Total de salário pago: ', salario_total)
    if comissao_lista:
        print('Média das comissões: ', sum(comissao_lista) / len(comissao_lista))
        print(f'Maior comissão: {max(comissao_lista)} || Menor comissão: {min(comissao_lista)}')
    else:
        print('Nenhuma comissão foi registrada.')

main()