class Bike:
    def __init__(self, velocidade, marcha, cadencia, numSerie):
        self.velocidade = velocidade
        self.marcha = marcha
        self.cadencia = cadencia
        self.numSerie = numSerie

    def get_velocidade(self):
        return self.velocidade

    def __str__(self):
        return (f"Bicicleta {self.numSerie}: Velocidade = {self.velocidade}, "
                f"Marcha = {self.marcha}, Cadência = {self.cadencia}")

class Comparador:
    def comparar(self, bicicleta1, bicicleta2):
        raise NotImplementedError("Método deve ser implementado pela subclasse.")

class ComparadorPorVelocidade(Comparador):
    def comparar(self, bicicleta1, bicicleta2):
        if bicicleta1.get_velocidade() < bicicleta2.get_velocidade():
            return "A velocidade da Bicicleta 2 é maior que a da Bicicleta 1"
        elif bicicleta1.get_velocidade() == bicicleta2.get_velocidade():
            return "A velocidade da Bicicleta 1 é igual à da Bicicleta 2"
        else:
            return "A velocidade da Bicicleta 1 é maior que a da Bicicleta 2"

class SistemaDeBicicletas:
    def __init__(self):
        self.bicicletas = []

    def criar_bike(self, num):
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
                    self.bicicletas.append(bike)
                    break
            except ValueError:
                print("Insira um número válido!")

    def comparar_bicicletas(self):
        if len(self.bicicletas) < 2:
            print("É necessário criar pelo menos duas bicicletas para comparação.")
            return
        
        comparador = ComparadorPorVelocidade()
        resultado = comparador.comparar(self.bicicletas[0], self.bicicletas[1])
        
        print(resultado)
        for bike in self.bicicletas:
            print(bike)

def main():
    sistema = SistemaDeBicicletas()
    sistema.criar_bike("1")
    sistema.criar_bike("2")
    sistema.comparar_bicicletas()

main()
