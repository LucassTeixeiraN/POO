# Uma empresa está fazendo um estudo de possibilidades de aumento aos seus
# funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à
# todos os funcionários ou seguir a seguinte tabela progressiva:
# Salário Percentual de aumento
# até R$1000,00 15%
# até R$2000,00 10%
# acima de R$2000,00 5%

# Faça um programa que leia o salário de um número qualquer de funcionários,
# imprimindo para cada um o novo salário nos dois casos (aumento uniforme ou
# aumento progressivo). Ao final, o programa deve fornecer:
# a. O total de funcionários
# b. O salário médio dos funcionários
# c. O total da folha de pagamentos atual
# d. O total da folha de pagamentos futura nos dois casos estudados, indicando
# qual o caminho mais econômico para a empresa.

def totalFunc(salarios):
    n_funcionarios = 0
    for i in salarios:
        n_funcionarios += 1

    return n_funcionarios 

def folhaPagamento(salarios):
    soma_salarios = 0
    for i in salarios:
        soma_salarios += i
    
    return soma_salarios

def salarioMedio(salarios):
    n_funcionarios = totalFunc(salarios)
    soma_salarios = folhaPagamento(salarios)
    
    return soma_salarios/n_funcionarios

def aumento_uniforme(salario):
    return salario * 1.10

def aumento_progressivo(salario):
    if salario <= 1000:
        return salario * 1.15
    elif salario <= 2000:
        return salario * 1.1
    else:
        return salario * 1.05

def main():
    salarios = []
    total_uniforme = 0
    total_progressivo = 0

    print("-"*60)
    while True:
        try:
            salario = float(input("Insira o salário do funcionário (digite 0 caso não haja mais funcionários): "))
            if salario == 0:
                break
            elif salario > 0:
                salarios.append(salario)
                sal_aumento_uniforme = aumento_uniforme(salario)
                sal_aumento_prog = aumento_progressivo(salario)
                print(f"Novo salário após o aumento uniforme: {sal_aumento_uniforme:.2f}")
                print(f"Novo salário após o aumento progressivo: {sal_aumento_prog:.2f}")
                print("-"*60)
                total_uniforme += sal_aumento_uniforme
                total_progressivo += sal_aumento_prog
            else:
                print("Valor inválido")

        except ValueError:
            print("Valor inválido")

    print("-"*60)
    print(f"Total de funcionários: {totalFunc(salarios)}")
    print(f"Salário médio dos funcionários: {salarioMedio(salarios):.2f}")
    print(f"Total da folha de pagamento atual: {folhaPagamento(salarios):.2f}")
    print(f"Total da folha de pagamento após o aumento uniforme: {total_uniforme:.2f}")
    print(f"Total da folha de pagamento após o aumento progressivo: {total_progressivo:.2f}")
    if total_uniforme < total_progressivo:
        print("O aumento uniforme será mais vantajoso para a empresa")
    else:
        print("O aumento progressivo será mais vantajoso para a empresa")

    print("-"*60)

main()
