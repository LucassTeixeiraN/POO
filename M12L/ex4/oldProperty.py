from property import Property

class OldProperty(Property):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def get_desconto(self):
        return self.desconto

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'Desconto: {self.desconto}')