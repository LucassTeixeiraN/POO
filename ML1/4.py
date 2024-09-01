"""Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite."""

def idade_input():
    try:
        valor = float(input("Digite a idade do aluno: "))
        return valor
    except:
        print("Número inválido. Digite novamente!")
        return idade_input()

def main():
    idades = []
    while True:
        idade = idade_input()
        
        if idade == 0:
            break
        if idade < 0:
            print("Redigite a idade do aluno.")
            continue
        
        idades.append(idade)
        
    print(f"A média da idade dos alunos é {sum(idades) / len(idades)}")

main()