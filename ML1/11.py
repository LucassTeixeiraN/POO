# O volume de uma esfera pode ser calculado pela fórmula
# V = (4/3)πr³, onde r é o raio da
# esfera. Faça um programa que imprima uma tabela de volumes para esferas que
# tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.

PI = 3.14

def calcVolume(raio):
    volume = (4*PI*(raio**3))/3
    return volume

def geradRaios(começo, limite, passo):
    raios = []
    for i in range(começo, limite+1, passo):
        raios.append(i)
    return raios

def tabela():
    raios = geradRaios(0, 150, 5)
    for i in raios:
        print("%13s%16s"%(f"{i/10}cm",f"{calcVolume(i/10):.2f}cm³"))

def main():
    print("%13s%15s"%("Raio", "Volume"))
    tabela()
main()
