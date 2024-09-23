"""Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice."""

class Invoice:

    def __init__(self, numItem, descricao, quantidade, preco):
        self.numeroItem = numItem
        self.descricaoItem = descricao
        
       
        if self.verif_maior_zero(quantidade):
            self.quantidadeComprada = quantidade
        else:
            self.quantidadeComprada = 0
        
       
        if self.verif_maior_zero(preco):
            self.precoItem = preco
        else:
            self.precoItem = 0

    @staticmethod
    def verif_maior_zero(num):
        return num > 0

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
    print("-" *20, "CADASTRO DE ITEMS", "-" *20, "\n")

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
main()
