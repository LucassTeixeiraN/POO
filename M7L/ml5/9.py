class Invoice:

    def __init__(self, numItem, descricao, quantidade, preco):
        self.__numeroItem = numItem
        self.__descricaoItem = descricao
        
        if self.verif_maior_zero(quantidade):
            self.__quantidadeComprada = quantidade
        else:
            self.__quantidadeComprada = 0
        
        if self.verif_maior_zero(preco):
            self.__precoItem = preco
        else:
            self.__precoItem = 0

    @staticmethod
    def verif_maior_zero(num):
        return num > 0

    def set_numeroItem(self, numItem):
        self.__numeroItem = numItem
    
    def set_descricaoItem(self, descricao):
        self.__descricaoItem = descricao

    def set_quantidadeComprada(self, quantidade):
        if self.verif_maior_zero(quantidade):
            self.__quantidadeComprada = quantidade
        else:
            self.__quantidadeComprada = 0

    def set_precoItem(self, preco):
        if self.verif_maior_zero(preco):
            self.__precoItem = preco
        else:
            self.__precoItem = 0

    def get_numeroItem(self):
        return self.__numeroItem
    
    def get_descricaoItem(self):
        return self.__descricaoItem
    
    def get_quantidadeComprada(self):
        return self.__quantidadeComprada
    
    def get_precoItem(self):
        return self.__precoItem
    
    def calcularFatura(self):
        return self.__quantidadeComprada * self.__precoItem
 
    def calcularImposto(self):
        return self.calcularFatura() * 1.10
    
class Periferico(Invoice):
    def calcularImposto(self):
        return self.calcularFatura() * 1.25

class PecaHardware(Invoice):
    def calcularImposto(self):
        return self.calcularFatura() * 1.13

class EquipamentoAudio(Invoice):
    def calcularImposto(self):
        return self.calcularFatura() * 1.05

class IoT(Invoice):
    def calcularImposto(self):
        return self.calcularFatura() * 1.2

def main():
    produtos = []
    continuarCadastrando = "S"
    print("-" * 20, "CADASTRO DE ITEMS", "-" * 20, "\n")

    while continuarCadastrando.upper() == "S":
        numItem = int(input("\nDigite o número do item: "))
        descricao = input("Digite a descrição do item: ")
        quantidade = int(input("Digite a quantidade comprada do item: "))
        preco = float(input("Digite o preço unitário do item: R$ "))

        print("\nEscolha o tipo de produto:")
        print("1 - Periférico")
        print("2 - Peça de Hardware")
        print("3 - Equipamento de Áudio")
        print("4 - IoT")
        print("5 - Outro (genérico)")
        
        tipo = int(input("Digite o número correspondente ao tipo de produto: "))

        if tipo == 1:
            produto = Periferico(numItem, descricao, quantidade, preco)
        elif tipo == 2:
            produto = PecaHardware(numItem, descricao, quantidade, preco)
        elif tipo == 3:
            produto = EquipamentoAudio(numItem, descricao, quantidade, preco)
        elif tipo == 4:
            produto = IoT(numItem, descricao, quantidade, preco)
        else:
            produto = Invoice(numItem, descricao, quantidade, preco) 

        produtos.append(produto)

        continuarCadastrando = input("\nDeseja cadastrar outro produto? (S/n): ")

    print("\nFaturas cadastradas: ")
    for i, invoice in enumerate(produtos, start=1):
        print(f"\nFatura {i}:")
        print(f"Número do Item: {invoice.get_numeroItem()}")
        print(f"Descrição: {invoice.get_descricaoItem()}")
        print(f"Quantidade: {invoice.get_quantidadeComprada()}")
        print(f"Preço Unitário: R${invoice.get_precoItem():.2f}")
        print(f"Valor Total da Fatura: R${invoice.calcularFatura():.2f}")
        print(f"Valor Total com Imposto: R${invoice.calcularImposto():.2f}")

main()
