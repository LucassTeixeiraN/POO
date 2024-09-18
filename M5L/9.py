

class Invoice:
    
    def __init__(self, numItem, descricao, quantidade, preco):
        self.numeroItem = numItem
        self.descricaoItem = descricao
        
        if quantidade > 0:
            self.quantidadeComprada = quantidade
        else:
            self.quantidadeComprada = 0
        
       
        if preco > 0:
            self.precoItem = preco
        else:
            self.precoItem = 0

    def set_numeroItem(self, numItem):
        self.numeroItem = numItem
    
    def set_descricaoItem(self, descricao):
        self.descricaoItem = descricao

    def set_quantidadeComprada(self, quantidade):
        self.quantidadeComprada = quantidade

    def set_precoItem(self, preco):
        self.precoItem = preco

 
    def get_numeroItem(self):
        return self.numeroItem
    
    def get_descricaoItem(self):
        return self.descricaoItem
    
    def get_quantidadeComprada(self):
        return self.quantidadeComprada
    
    def get_precoItem(self):
        return self.precoItem
    
   
    def calcularFatura(self):
        return self.quantidadeComprada * self.precoItem

def main():
    produtos = []
    continuarCadastrando = "S"
    print("-" *20, "CADASTRO DE ITEMS", "-" *20, "\n\n")

    while continuarCadastrando.upper() == "S":
            numItem = int(input("\nDigite o número do item: "))
            descricao = input("Digite a descrição do item: ")
            quantidade = int(input("Digite a quantidade comprada do item: "))
            preco = float(input("Digite o preço unitário do item: R$ "))

            invoiceProduct = Invoice(numItem, descricao, quantidade, preco)
            produtos.append(invoiceProduct) 

            continuarCadastrando = input("\nDeseja cadastrar outro produto? (S/n): ")

    print("\n Faturas cadastradas: ")
    for i, invoice in enumerate(produtos, start=1):
        print(f"\nFatura {i}:")
        print(f"Número do Item: {invoice.get_numeroItem()}")
        print(f"Descrição: {invoice.get_descricaoItem()}")
        print(f"Quantidade: {invoice.get_quantidadeComprada()}")
        print(f"Preço Unitário: R${invoice.get_precoItem():.2f}")
        print(f"Valor Total da Fatura: R${invoice.calcularFatura():.2f}")
