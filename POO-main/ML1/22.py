"""

O que precisa ser recebido 
- nº cpf -> V
- nº de dependentes -> V
- salário mensal -> V

Regras
- CPF = 0 parar o programa. -> v
- Cada dependente diminui 136R$ no total do imposto -> V

Printar
- Valor do imposto total
- Número de contribuintes
- Total de contribuintes isentos e não isento
- O valor total ganho
- O número do CPF e o valor de contribuição de quem for pagar o maior imposto

"""

registroDeContribuintes = []
def cadastrarContribuinte():
    global registroDeContribuintes
    cpf = input("Insira o número do CPF do contribuinte (digite 0 para parar): ")

    if(cpf == "0"):
        print("RESULTADOS ---------")
        exibirResultados(registroDeContribuintes)
    else:
        dependentes = int(input("Digite o número de Dependentes do contribuinte: "))
        salario = float(input("Digite o salário do contribuinte: "))
        imposto = calcularImposto(salario, dependentes)
        registroDeContribuintes = armazenarContribuinte(cpf, salario, dependentes, imposto)
        cadastrarContribuinte()

def calcularImposto(salario, dependentes):
    if(0 < salario <= 900):
        imposto = 0
    elif(900 < salario <= 1500):
        imposto = salario * 0.05
    elif(1500 < salario <= 1900):
        imposto = salario * 0.1
    elif(1900 < salario <= 2200):
        imposto = salario * 0.15
    elif(salario > 2200):
        imposto = salario * 0.2
    else:
        print("Insira um valor de salário válido! ")
        cadastrarContribuinte()
        return
    
    imposto = imposto - 136 * dependentes
    
    if(imposto < 0):
        imposto = 0

    return imposto

def armazenarContribuinte(cpf, salario, dependentes, imposto):
    registroDeContribuintes.append([cpf, salario, dependentes, imposto])
    return registroDeContribuintes
     
def exibirResultados(registros):
    for registro in registros:
        print(f"CPF: {registro[0]},  Salário: R$ {registro[1]}, Dependentes: {registro[2]}, Imposto: R$ {registro[3]}")

    imposto_total = sum(registro[3] for registro in registros)
    print(f"\nValor total do imposto: {imposto_total}")

    numero_contribuintes = len(registros)
    print(f"\nNúmero de contribuintes: {numero_contribuintes}")

    isentos = sum(1 for registro in registros if registro[3] == 0)
    nao_isentos = numero_contribuintes - isentos
    print(f"\nTotal de contribuintes isentos: {isentos}")
    print(f"Total de contribuintes não isentos: {nao_isentos}")

    maior_imposto = max(registros, key=lambda x: x[3])
    cpf_maior_imposto = maior_imposto[0]
    valor_maior_imposto = maior_imposto[3]
    print(f"\n O CPF do contribuinte que paga o maior imposto é {cpf_maior_imposto}, com o valor de {valor_maior_imposto}")


cadastrarContribuinte()
