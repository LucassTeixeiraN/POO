'''Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
acumulados. Faça um programa que compute o progresso do aluno, através da
leitura de suas notas até que ele termine o 10o nível. Utilize o comando break (por
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
máxima).'''

def coletarNota():
    while True:
        try:
            nota = int(input("Insira a nota do aluno(0-100): "))
            if nota >= 0:
                return nota
            print("Valor inválido")
            continue
        except ValueError:
            print("Valor inválido")
            
def subirNivel(nota):
    if nota >= 100:
        return True
    return False

    
def main():
    nivel = 1
    tentativa = 1
    nota_acumulada = nota_nivel_acumulada = 0
    while True:
        nota_nivel = coletarNota()
        nota_nivel_acumulada += nota_nivel
        nota_acumulada += nota_nivel
        
        
        if tentativa == 5 and nivel > 1:
            if nota_acumulada < 300:
                print("Voltando um nível.")
                nivel -= 1
            nota_acumulada = 0
            tentativa = 0
        elif tentativa == 5 and nivel <= 1:
            nota_acumulada = 0
            tentativa = 0
        elif subirNivel(nota_nivel_acumulada):
            print("Parabéns! Você subiu de nivel.")
            nivel += 1
            tentativa = 0
            nota_nivel_acumulada = 0
        else:
            tentativa += 1
        
        if nivel == 10:
            print("Você venceu! Parabéns!")
            break
        print(f"Pontos acumulados: {nota_acumulada}")
        print(f"Nível: {nivel}")
            
main()
