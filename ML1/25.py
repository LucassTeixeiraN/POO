'''Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual foram coletados os seguintes dados referentes a cada habitante
para serem analisados:
• Sexo.
• Cor dos olhos (azuis, verdes, castanhos).
• Cor dos cabelos (louros, castanhos, pretos).
• Idade.
Faça um programa que determine e escreva:
a. O total de entrevistados
b. O total de homens e o total de mulheres entrevistados
c. A maior e a menor idade do conjunto de habitantes;
d. A média de idade do conjunto de habitantes;
e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.'''

def input_usuario():
    habitantes = []
    
    while True:
        idade = int(input("Digite a idade (ou -1 para encerrar): "))
        if idade == -1:
            break

        sexo = input("Digite o sexo (M/F): ").strip().upper()
        cor_olhos = input("Digite a cor dos olhos (azuis, verdes, castanhos): ").strip().lower()
        cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos, pretos): ").strip().lower()

        habitantes.append({
            "idade": idade,
            "sexo": sexo,
            "cor_olhos": cor_olhos,
            "cor_cabelos": cor_cabelos
        })
    
    return habitantes

def calcula_estatisticas(habitantes):
    total_entrevistados = len(habitantes)
    total_homens = total_mulheres = 0
    idades = []
    total_mulheres_18_35 = 0
    
    for habitante in habitantes:
        idade = habitante["idade"]
        sexo = habitante["sexo"]
        cor_olhos = habitante["cor_olhos"]
        cor_cabelos = habitante["cor_cabelos"]
        
        if sexo == 'M':
            total_homens += 1
        elif sexo == 'F':
            total_mulheres += 1
            if 18 <= idade <= 35 and cor_olhos == 'verdes' and cor_cabelos == 'louros':
                total_mulheres_18_35 += 1
        
        idades.append(idade)
    
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idade = sum(idades) / total_entrevistados
    percentual_mulheres_18_35 = total_mulheres_18_35 / total_mulheres * 100
    
    return total_entrevistados, total_homens, total_mulheres, maior_idade, menor_idade, media_idade, percentual_mulheres_18_35



def exibe_resultados(total_entrevistados, total_homens, total_mulheres, maior_idade, menor_idade, media_idade, percentual_mulheres_18_35):
    print(f"Total de entrevistados: {total_entrevistados}")
    print(f"Total de homens: {total_homens}")
    print(f"Total de mulheres: {total_mulheres}")
    print(f"Maior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Percentagem de mulheres de 18 a 35 anos com olhos verdes e cabelos louros: {percentual_mulheres_18_35:.2f}%")

def main():
    habitantes = input_usuario()
    estatisticas = calcula_estatisticas(habitantes)
    exibe_resultados(*estatisticas)

main()