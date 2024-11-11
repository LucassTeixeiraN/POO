# Crie uma classe Product que possua atributos para nome e preço, crie os métodos
# sets e gets para estes atributos. Crie também um atributo para descrição e seu
# método chamado get que retorna uma string com um conteúdo simples como
# “Produto de informática”. Crie duas classes filhas de Product, que serão Mouse com
# atributo para o tipo e Book com um atributo para o author; no método construtor de
# cada uma dessas classes passe como argumento a descrição do produto, por
# exemplo, Mouse (“Mouse ótico, Saída USB. 1.600 dpi”). Crie um método get que
# retorna a descrição que foi passada no argumento do construtor concatenada com o
# atributo que a classe tiver, author no caso de livro e type no caso de mouse. Esse
# método deve ter a mesma assinatura do método get da classe pai Product. Crie um
# script “main” que irá simular a compra de um cliente de vários mouses e livros, deve
# haver apenas uma lista no main.py para armazenamento de todos os livros e mouses.
# Essa lista deve simular o carrinho de compras de produtos variados de um cliente em
# um e-commerce. Insira nesse carrinho vários mouses e livros e depois chame o
# método get de todos os objetos presentes na lista, para o usuário do carrinho saber
# as informações dos produtos em seu carrinho.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._description = "Produto de informática"

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description


class Mouse(Product):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self._type = type

    def get_description(self):
        return f"{super().get_description()} - Tipo: {self._type}"


class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self._author = author

    def get_description(self):
        return f"{super().get_description()} - Autor: {self._author}"


def main():
    cart = [
        Mouse("Mouse ótico", 50.0, "Saída USB. 1.600 dpi"),
        Book("Python Programming", 100.0, "John Doe"),
        Mouse("Mouse sem fio", 70.0, "Wireless. 2.400 dpi"),
        Book("Data Science", 120.0, "Jane Smith")
    ]

    for item in cart:
        print(item.get_description())
main()
