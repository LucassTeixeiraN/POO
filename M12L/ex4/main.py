'''Crie a classe Property, que possui um endereço e um preço.
a. Crie uma classe NewProperty, que herda Property e possui um adicional no
preço. Crie métodos de acesso e impressão deste valor adicional.
b. Crie uma classe OldProperty, que herda Property e possui um desconto no
preço. Crie métodos de acesso e impressão para este desconto.'''

from newProperty import NewProperty
from oldProperty import OldProperty

def main():
    nova_propriedade = NewProperty("Rua Nova, 123", 300000, 20000)
    nova_propriedade.imprimir_informacoes()

    print()  

    propriedade_antiga = OldProperty("Rua Velha, 456", 250000, 30000)
    propriedade_antiga.imprimir_informacoes()

if __name__ == "__main__":
    main()