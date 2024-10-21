
# Crie uma classe Invoice para que uma loja de suprimentos de informática possa
# utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve
# incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
# a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
# um construtor que inicializa as quatro variáveis de instância. Forneça um método set
# e um get para cada variável de instância. Forneça também um método chamado que
# calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
# resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
# configurada como 0. Se o preço do item não for positivo, deve ser configurado como
# # 0.0. Teste a classe implementada e seus métodos.

class Fatura:
    def __init__(self, numSerie, descricao, quantidade, preco):
        self.__numSerie = numSerie
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__preco = preco

    def setNumero(self, numSerie):
        self.__numSerie = numSerie

    def getNumero(self):
        return self.__numSerie

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao

    def setQuantidade(self, quantidade):
        if quantidade > 0:
            self.__quantidade = quantidade
        else:
            self.__quantidade = 0

    def getQuantidade(self):
        return self.__quantidade

    def setPreco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            self.__preco = 0.0

    def getPreco(self):
        return self.__preco

    def calcularTotal(self):
        return self.__quantidade * self.__preco

class FaturaComDesconto:
    def __init__(self, numSerie, descricao, quantidade, preco, desconto):
        self.fatura = Fatura(numSerie, descricao, quantidade, preco)
        self.__desconto = desconto

    def calcularTotal(self):
        total = self.fatura.calcularTotal()
        return total - (total * (self.__desconto / 100))

    def getNumero(self):
        return self.fatura.getNumero()

    def getDescricao(self):
        return self.fatura.getDescricao()

    def getQuantidade(self):
        return self.fatura.getQuantidade()

    def getPreco(self):
        return self.fatura.getPreco()
        
def main():
    fatura = Fatura("999", "Bicicleta", 7, 999.99)
    print(f"Numero: {fatura.getNumero()}")
    print(f"Descricao: {fatura.getDescricao()}")
    print(f"Quantidade: {fatura.getQuantidade()}")
    print(f"Preco por item: {fatura.getPreco()}")
    print(f"Total: {fatura.calcularTotal()}")

    fatura_com_desconto = FaturaComDesconto("1000", "Cadeira", 5, 199.99, 10)
    print(f"\nNumero: {fatura_com_desconto.getNumero()}")
    print(f"Descricao: {fatura_com_desconto.getDescricao()}")
    print(f"Quantidade: {fatura_com_desconto.getQuantidade()}")
    print(f"Preco por item: {fatura_com_desconto.getPreco()}")
    print(f"Total com desconto: {fatura_com_desconto.calcularTotal()}")

main()
