from automovel import Automovel
from motorcycle import Moto
from truck import Caminhao

def main():
    veiculos = [
        Automovel("Tesla", "Model 3", 2021, 4, 75, True),
        Moto("Kawasaki", "Ninja 400", 2020, 399),
        Caminhao("Mercedes", "Actros", 2019, 20000)
    ]

    for veiculo in veiculos:
        print(veiculo.exibir_info())

if __name__ == "__main__":
    main()

# Interfaces: Definem contratos que as classes de veículos devem seguir, garantindo que implementem métodos específicos relacionados às suas funcionalidades (como informações sobre bateria e teto solar).