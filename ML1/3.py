'''Em um frigorífico, cada boi é identificado por um cartão que contém seu número e
seu peso. Faça um programa que leia os números de identificação e o peso de cada
boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi
mais magro e o total de peso dos bois do frigorífico.'''

def registrarBoi():
    bois = {}
    while True:
        try:
            numero = int(input("Insira o número do boi (Digite 0 para finalizar o registro): "))
            if numero == 0:
                break
            elif not numero in bois: 
                peso = float(input("Insira o peso desse boi: "))
                if peso > 0:
                    bois[numero] = peso
                else:
                    print("Peso inválido")
            else:
                print("Já existe um boi com essa numeração")
        except ValueError:
            print("Valores inválidos")
    return bois
    
def maisPesado(bois_dict):
    maior_peso = 0
    for chave, valor in bois_dict.items():
        if valor > maior_peso:
            maior_peso = valor
            numero_mais_pesado = chave

    return (numero_mais_pesado, maior_peso)

def maisMagro(bois_dict):
    menor_peso = 0
    for chave, valor in bois_dict.items():
        if valor < menor_peso or menor_peso == 0:
            menor_peso = valor
            numero_mais_leve = chave
    
    return (numero_mais_leve, menor_peso)

def pesoTotal(bois_dict):
    peso_soma = 0
    for valor in bois_dict.values():
        peso_soma += valor
    
    return peso_soma

def main():
    bois_dict = registrarBoi()
    print("-"*60)
    print(f"O boi mais gordo era o de numeração {maisPesado(bois_dict)[0]}, pesando {maisPesado(bois_dict)[1]} kg.")
    print(f"O boi mais magro era o de numeração {maisMagro(bois_dict)[0]}, pesando {maisMagro(bois_dict)[1]} kg.")
    print(f"Somados, todos os bois pesam {pesoTotal(bois_dict)} kg.")
    print("-"*60)
main()
