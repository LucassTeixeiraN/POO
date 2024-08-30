'''Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
acumulados. Faça um programa que compute o progresso do aluno, através da
leitura de suas notas até que ele termine o 10o nível. Utilize o comando break (por
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
máxima).'''
def ler_nota():
    while True:
        try:
            nota = int(input("Digite a nota (0-100): "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def verificar_progresso(nivel_atual, pontos_acumulados, tentativas):
    if pontos_acumulados >= 100:
        print("Parabéns, você passou para o próximo nível!")
        return nivel_atual + 1, 0, 0
    elif tentativas == 5 and pontos_acumulados < 300:
        print("Você não alcançou a pontuação mínima, voltando ao nível anterior.")
        return nivel_atual - 1, 0, 0
    else:
        return nivel_atual, pontos_acumulados, tentativas

def main():
    nivel_atual = 1
    pontos_acumulados = 0
    tentativas = 0

    while nivel_atual <= 10:
        while True:
            print(f"Nível {nivel_atual}:")
            nota = ler_nota()
            pontos_acumulados += nota
            tentativas += 1
            nivel_atual, pontos_acumulados, tentativas = verificar_progresso(nivel_atual, pontos_acumulados, tentativas)
            if nivel_atual > 10:
                break
            elif pontos_acumulados >= 100:
                break

        if nivel_atual == 10 and pontos_acumulados >= 100:
            print("Parabéns, você concluiu o 10º nível!")
            break
main()        


# fodase nao to conseguindo essa merda