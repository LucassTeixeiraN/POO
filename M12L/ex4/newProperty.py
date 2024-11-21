from property import Property

class NewProperty(Property):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def get_adicional(self):
        return self.adicional

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'Adicional: {self.adicional}')