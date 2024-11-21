class Imovel:
    def __init__(self, estado):
        self.estado = estado

    def valor(self):
        if self.estado == 1:
            return 200000  # Novo
        elif self.estado == 2:
            return 100000  # Velho
        return 0