class FaturaComDesconto:  
    pass

class Fatura:
    def __init__(self, numSerie, descricao, quantidade, preco):
        self.__numSerie = numSerie
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__preco = preco
        self.__faturaComDesconto = None  #Inicializa a referência

    def setFaturaComDesconto(self, faturaComDesconto):
        self.__faturaComDesconto = faturaComDesconto

    def getNumero(self):
        return self.__numSerie

    def calcularTotal(self):
        total = self.__quantidade * self.__preco
        if self.__faturaComDesconto:  
            total = self.__faturaComDesconto.aplicarDesconto(total)
        return total

    def getDescricao(self):
        return self.__descricao

    def getQuantidade(self):
        return self.__quantidade

    def getPreco(self):
        return self.__preco


class FaturaComDesconto:
    def __init__(self, desconto, fatura):
        self.__desconto = desconto
        self.__fatura = fatura
        self.__fatura.setFaturaComDesconto(self)  #Estabelece a relação

    def aplicarDesconto(self, total):
        return total - (total * (self.__desconto / 100))

    def getDesconto(self):
        return self.__desconto


def main():
    fatura = Fatura("999", "Bicicleta", 7, 999.99)
    fatura_com_desconto = FaturaComDesconto(10, fatura)

    print(f"Numero: {fatura.getNumero()}")
    print(f"Descricao: {fatura.getDescricao()}")
    print(f"Quantidade: {fatura.getQuantidade()}")
    print(f"Preco por item: {fatura.getPreco()}")
    print(f"Total com desconto: {fatura.calcularTotal()}")


main()
