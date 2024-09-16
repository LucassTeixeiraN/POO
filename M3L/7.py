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
        self.__numSerie: str = numSerie
        self.__descricao: str = descricao
        self.__quantidade: int = quantidade
        self.__preco: float = preco

    def setNumero(self, numero):
        self.__numSerie = numero

    def getNumero(self) -> str:
        return self.__numSerie

    def setDescricao(self, descricao) :
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

    def getPreco(self) -> float:
        return self.__preco

    def calcularTotal(self):
        return self.__quantidade * self.__preco

def main():
    
    fatura = Fatura("999", "Bicicleta", 7, 999.99)
    
    print(f"Numero: {fatura.getNumero()}")
    print(f"Descricao: {fatura.getDescricao()}")
    print(f"Quantidade: {fatura.getQuantidade()}")
    print(f"Preco por item: {fatura.getPreco()}")
    print(f"Total: {fatura.calcularTotal()}")
    
main()
