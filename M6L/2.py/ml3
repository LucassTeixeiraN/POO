class Bike:
    def __init__(self, velocidade, marcha, cadencia, numSerie):
        self.velocidade = velocidade
        self.marcha = marcha
        self.cadencia = cadencia
        self.numSerie = numSerie

    def getVelocidade(self):
        return self.velocidade

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.bike = None

    def adicionarBike(self, bike):
        self.bike = bike

def criarBike(num):
    while True:
        try:
            velocidade = float(input(f"Insira a velocidade da bicicleta de {num}: "))
            marcha = int(input(f"Insira a marcha atual da bicicleta {num}: "))
            cadencia = int(input(f"Insira a cadência (RPM) da bike {num}: "))
            numSerie = int(input(f"Insira o número de série da bicicleta {num}: "))
            if velocidade < 0 or marcha < 0 or marcha > 18 or cadencia < 0 or numSerie <= 1000:
                print("Algum(ns) valor(es) estão incorreto(s). Favor preencha-os corretamente!")
            else:
                return Bike(velocidade, marcha, cadencia, numSerie)
        except ValueError:
            print("Insira um número válido!")

def comparar(bicicleta1, bicicleta2, pessoa1, pessoa2):
    velocidade1 = bicicleta1.getVelocidade()
    velocidade2 = bicicleta2.getVelocidade()
    
    if velocidade1 < velocidade2:
        print(f"{pessoa2.nome} é mais rápido que {pessoa1.nome}.")
    elif velocidade1 == velocidade2:
        print(f"A velocidade é igual entre {pessoa1.nome} e {pessoa2.nome}.")
    else:
        print(f"{pessoa1.nome} é mais rápido que {pessoa2.nome}.")

def main():
    pessoa1 = Pessoa(input("Insira o nome da pessoa 1: "))
    pessoa2 = Pessoa(input("Insira o nome da pessoa 2: "))
    
    bicicleta1 = criarBike("1")
    bicicleta2 = criarBike("2")
    
    pessoa1.adicionarBike(bicicleta1)
    pessoa2.adicionarBike(bicicleta2)
    
    comparar(pessoa1.bike, pessoa2.bike, pessoa1, pessoa2)


main()
