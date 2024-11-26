class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = []

    def adicionar_veiculo(self, veiculo):
        self.estoque.append(veiculo)

    def listar_veiculos(self):
        if not self.estoque:
            return "Nenhum veículo disponível."
        return "\n".join(veiculo.display_info() for veiculo in self.estoque)