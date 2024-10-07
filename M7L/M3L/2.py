class Bike:
    def __init__(self, velocidade, marcha, cadencia, numSerie):
        self.velocidade = velocidade
        self.marcha = marcha
        self.cadencia = cadencia
        self.numSerie = numSerie

    def getVelocidade(self):
        return self.velocidade

    def __str__(self):
        return (f"Bicicleta {self.numSerie}: Velocidade = {self.velocidade}, "
                f"Marcha = {self.marcha}, Cadência = {self.cadencia}")


class Comparador:
    def comparar(self):


class ComparadorPorVelocidade(Comparador):
    def comparar(self, bicicleta1, bicicleta2):
        if bicicleta1.getVelocidade() < bicicleta2.getVelocidade():
            return "A velocidade da Bicicleta 2 é maior que a da Bicicleta 1"
        elif bicicleta1.getVelocidade() == bicicleta2.getVelocidade():
            return "A velocidade da Bicicleta 1 é igual à da Bicicleta 2"
        else:
            return "A velocidade da Bicicleta 1 é maior que a da Bicicleta 2"


def criarBike(num):
    while True:
        try:
            velocidade = float(input(f"Insira a velocidade da bicicleta {num}: "))
            marcha = int(input(f"Insira a marcha atual da bicicleta {num}: "))
            cadencia = int(input(f"Insira a cadência (RPM) da bike {num}: "))
            numSerie = int(input(f"Insira o número de série da bicicleta {num}: "))
            if (velocidade < 0 or marcha < 0 or marcha > 18 or cadencia < 0 or numSerie < 1000):
                print("Algum(ns) valor(es) estão incorreto(s). Favor preencha-os corretamente!")
            else:
                return Bike(velocidade, marcha, cadencia, numSerie)
        except ValueError:
            print("Insira um número válido!")


def main():
    bicicleta1 = criarBike("1")
    bicicleta2 = criarBike("2")
    
    comparador = ComparadorPorVelocidade()
    resultado = comparador.comparar(bicicleta1, bicicleta2)
    
    print(resultado)
    print(bicicleta1)
    print(bicicleta2)

main()
