
# 2. Escreva uma classe chamada Bicycle que possua campos para a velocidade,
# cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
# número de série. A velocidade e a cadência dos pedais não podem ser menores que
# zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
# 1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
# esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
# que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
# o seu novo método.

class Bike:
    def __init__(self, velocidade, marcha, cadencia, numSerie):
        self.velocidade = velocidade
        self.marcha = marcha
        self.cadencia = cadencia
        self.numSerie = numSerie

    def getVelocidade(self):
        return self.velocidade
    

def criarBike(num):
    while True:
        try:
            velocidade = float(input("Insira a velocidade da bicicleta " + num + ": "))
            marcha = int(input("Insira a marcha atual da bicicleta" + num + ": "))
            cadencia = int(input("Insira a cadência (RPM) da bike" + num +": "))
            numSerie = int(input("Insira o número de série" + num + ": "))
            if velocidade < 0 or marcha < 0 or marcha > 18 or cadencia < 0 or numSerie < 1000:
                print("Algum(ns) valor(es) estão incorreto(s). Favor preencha-os corretamente!")
                criarBike()
            else:
                return Bike(velocidade, marcha, cadencia, numSerie)
        except ValueError :
            print("insira um número válido!")



def comparar(bicicleta1, bicicleta2):
    if(bicicleta1.getVelocidade() < bicicleta2.getVelocidade()):
        print("A velocidade da Bicicleta 2 é maior que a velocidade da Bicicleta 1")
    elif(bicicleta1.getVelocidade() == bicicleta2.getVelocidade()):
        print("A velocidade da Bicicleta 1 é igual a velocidade da Bicicleta 2")
    else:
        print("A velocidade da Bicicleta 1 é maior que a velocidade da Bicicleta 2")


def main():
    bicicleta1 = criarBike("1")
    bicicleta2 = criarBike("2")
    comparar(bicicleta1, bicicleta2)

main()
