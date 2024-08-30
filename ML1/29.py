'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo:

( 32)
9
5
C = F − . A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

def fPraC(F):
    C = 5/9*(F-32)
    return C

def main():
    print("-"*30,"Conversão de Temperatura", "-"*30)
    while True:
        try:
            F = int(input("Insira uma temperatura em graus F para saber seu equivalente em C: ")) 
            C = fPraC(F)
            print(f"{F}° = {C:.2f}°")
            x = input("Deseja fazer nova conversão?(s/n):")
            if x.lower() == "s":
                continue
            else:
                print("Saindo do programa.")
                break
        except(ValueError):
            print("ERRO: Insira dados validos.")
            
main()