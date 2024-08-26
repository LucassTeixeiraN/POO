'''Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno
precisa ter média do período (mp) igual ou superior a 7 pontos. Caso contrário, o
aluno será submetido a exame final, sendo a sua média final (mf) calculada pela
seguinte fórmula: mf = 0.6mp + 0.4ne, onde ne é a nota do exame. Essa média final
deverá então ser igual ou superior a 5 pontos para que o aluno seja aprovado. Por
outro lado, a média do período é calculada através da média das notas dos créditos,
cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o
número de créditos da disciplina, as notas dos créditos, e se necessário calcule a
nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar
todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de
notas (utilize aqui um comando break).'''

# Função para ler as notas dos créditos
def lerNota(num_creditos):
    """
    Lê as notas dos créditos e verifica se o aluno já está aprovado.
    
    Args:
        num_creditos (int): Número de créditos da disciplina.
    
    Returns:
        list: Lista de notas dos créditos.
    """
    notas = []
    for i in range(num_creditos):
        while True:
            try:
                # Lê a nota do crédito atual
                nota = float(input(f"Informe a nota do crédito {i+1}: "))
                if nota < 0 or nota > 10:
                    # Verifica se a nota é válida
                    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
                else:
                    # Adiciona a nota à lista de notas
                    notas.append(nota)
                    # Calcula a média do período
                    media_periodo = sum(notas) / num_creditos
                    if media_periodo >= 7:
                        # Verifica se o aluno já está aprovado
                        print("-"*33)
                        print("Parabéns! Você já está aprovado!")
                        print("-"*33)
                        return notas
                    break
            except ValueError:
                # Trata erro de entrada inválida
                print("Dados inválidos. Por favor, insira uma nota válida.")
    return notas

# Função para calcular a média do período
def calcucarMediaP(notas):
    """
    Calcula a média do período.
    
    Args:
        notas (list): Lista de notas dos créditos.
    
    Returns:
        float: Média do período.
    """
    media_periodo = sum(notas) / len(notas)
    return media_periodo

# Função para calcular a nota do exame
def calcularExame(media_periodo):
    """
    Calcula a nota do exame necessário para aprovação.
    
    Args:
        media_periodo (float): Média do período.
    
    Returns:
        float: Nota do exame necessário para aprovação.
    """
    nota_exame = (5 - 0.6 * media_periodo) / 0.4
    return nota_exame

# Função principal
def main():
    print('-'*25,'Calculo de Notas','-'*25)
    while True:
        try:
            # Lê o número de créditos da disciplina
            num_creditos = int(input("Informe o número de créditos da disciplina: "))
            if num_creditos > 0:
                # Lê as notas dos créditos
                notas = lerNota(num_creditos)
                # Calcula a média do período
                media_periodo = calcucarMediaP(notas)
                if media_periodo < 7:
                    # Calcula a nota do exame necessário para aprovação
                    nota_exame = calcularExame(media_periodo)
                    if nota_exame <= 10:
                        # Imprime a nota do exame necessário para aprovação
                        print("-"*67)
                        print(f"Você precisa tirar no mínimo {nota_exame:.2f} no exame final para ser aprovado.")
                        print("-"*67)
                        break
                    else:
                        # Imprime mensagem de reprovação
                        print("-"*66)
                        print(f"Infelizmente você foi reprovado. (Nota necessária no exame: {nota_exame:.2f})")
                        print("-"*66)
                        break
main()                      
