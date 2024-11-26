'''Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.'''


from car import Car
from motorcycle import Motorcycle
from truck import Truck
from concessionaria import Concessionaria

def main():
    # Cria uma concessionária
    concessionaria = Concessionaria("Concessionária XYZ")

    # Cria veículos
    carro = Car("Toyota", "Corolla", 2021, 4)
    moto = Motorcycle("Honda", "CB500", 2020, 500)
    caminhão = Truck("Volvo", "FH", 2019, 18000)

    # Adiciona veículos ao estoque da concessionária
    concessionaria.adicionar_veiculo(carro)
    concessionaria.adicionar_veiculo(moto)
    concessionaria.adicionar_veiculo(caminhão)

    # Lista os veículos disponíveis na concessionária
    print(f"Veículos disponíveis na {concessionaria.nome}:\n")
    print(concessionaria.listar_veiculos())

if __name__ == "__main__":
    main()

# a Concessionaria contém e gerencia uma coleção de objetos Vehicle.