'''Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.'''

from car import Automovel
from motorcycle import Moto
from truck import Caminhao

def main():
    veiculos = [
        Automovel("Toyota", "Corolla", 2021, 4, True),
        Moto("Honda", "CB500", 2020, 500),
        Caminhao("Volvo", "FH", 2019, 18000)
    ]

    for veiculo in veiculos:
        print(veiculo.exibir_info())

if __name__ == "__main__":
    main()


# Mixins: Permitem adicionar funcionalidades específicas (como capacidades elétricas ou recursos de teto solar) às classes de veículos sem alterar sua estrutura de herança principal.