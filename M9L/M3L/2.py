class SistemaDeBicicletas: 
    def __init__(self):
        self.bicicletas = []

    def appendBike(self, bike):
        self.bicicletas.append(bike)

    def mostrar_bicicletas_ordenadas(self):
        bicicletas_ordenadas = sorted(self.bicicletas, key=lambda bike: bike.get_velocidade())
        print("\nBicicletas ordenadas por velocidade:")
        for bike in bicicletas_ordenadas:
            print(bike)

class Bike:  
    def __init__(self, velocidade, marcha, cadencia, numSerie):
        self.velocidade = velocidade
        self.marcha = marcha
        self.cadencia = cadencia
        self.numSerie = numSerie
        self.sistema = None

    def get_velocidade(self):
        return self.velocidade

    def set_sistema(self, sistema: SistemaDeBicicletas):
        self.sistema = sistema

    def __str__(self):
        return (f"Bicicleta {self.numSerie}: Velocidade = {self.velocidade}, "
                f"Marcha = {self.marcha}, Cadência = {self.cadencia}")

    def mostrar_informacoes(self):
        print(f"Informações da {self}:")
        self.sistema.mostrar_bicicletas_ordenadas()  #Chama método do sistema


def criar_bike(num):
    while True:
        try:
            velocidade = float(input(f"Insira a velocidade da bicicleta {num}: "))
            marcha = int(input(f"Insira a marcha atual da bicicleta {num}: "))
            cadencia = int(input(f"Insira a cadência (RPM) da bike {num}: "))
            numSerie = int(input(f"Insira o número de série da bicicleta {num}: "))
            
            if (velocidade < 0 or marcha < 0 or marcha > 18 or cadencia < 0 or numSerie < 1000):
                print("Algum(ns) valor(es) estão incorreto(s). Favor preencha-os corretamente!")
            else:
                bike = Bike(velocidade, marcha, cadencia, numSerie)
                return bike
        except ValueError:
            print("Insira um número válido!")


def adicionar_bicicletas(sistema):
    while True:
        try:
            qtd = int(input("Quantas bicicletas você deseja adicionar? "))
            if qtd <= 0:
                print("Por favor, insira um número positivo.")
            else:
                for i in range(1, qtd + 1):
                    bike = criar_bike(i)
                    sistema.appendBike(bike)
                    bike.set_sistema(sistema)
                break
        except ValueError:
            print("Insira um número válido!")

def main():
    sistema = SistemaDeBicicletas()

    adicionar_bicicletas(sistema)
    sistema.mostrar_bicicletas_ordenadas()

main()
