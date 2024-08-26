'''Em um frigorífico, cada boi é identificado por um cartão que contém seu número e
seu peso. Faça um programa que leia os números de identificação e o peso de cada
boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi
mais magro e o total de peso dos bois do frigorífico.'''

def registrarBoi():
    bois = {}
    while True:
        try:
            numero = int(input("Insira o número do boi (Digite 0 para finalizar o registro)"))
            if numero == 0:
                break
            peso = float(input("Insira o peso desse boi"))
            bois[numero] = peso

        except ValueError:
            print("Valores inválidos")
    return bois
    
def maisPesado(bois_dict):
    mais_pesado = 0
    for chave, valor in bois_dict.items():
        if bois_dict[chave] > mais_pesado:
            mais_pesado = bois_dict[chave]
    return mais_pesado

def main():
    bois_dict = registrarBoi()
    print(maisPesado(bois_dict))
    

main()
