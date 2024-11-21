class Property:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_preco(self):
        return self.preco

    def get_endereco(self):
        return self.endereco

    def imprimir_informacoes(self):
        print(f'Endereço: {self.endereco}, Preço: {self.preco}')