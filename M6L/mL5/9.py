"""
Crie uma classe chamada Invoice que possa ser utilizado por uma loja de suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos.
Se a quantidade não for positiva, ela deve ser configurada como 0. 
Se o preço por item não for positivo ele deve ser configurado como 0.0. 
Forneça um método set e um método get para cada variável de instância. 
Além disso, forneça um método chamado que calcula o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna o valor real. 
Escreva um aplicativo de teste que demonstra as capacidades da classe Invoice.
"""

class Invoice:
    
    def __init__(self, numItem, descricao, quantidade, preco):
        self.numeroItem = numItem
        self.descricaoItem = descricao
        
        # Quantidade não Positiva = 0
        if quantidade > 0:
            self.quantidadeComprada = quantidade
        else:
            self.quantidadeComprada = 0
        
        # Preço não Positivo = 0
        if preco > 0:
            self.precoItem = preco
        else:
            self.precoItem = 0

    # Setters
    def set_numeroItem(self, numItem):
        self.numeroItem = numItem
    
    def set_descricaoItem(self, descricao):
        self.descricaoItem = descricao

    def set_quantidadeComprada(self, quantidade):
        self.quantidadeComprada = quantidade

    def set_precoItem(self, preco):
        self.precoItem = preco

    # Getters
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


class Pedido:
    
    def __init__(self, numeroPedido):
        self.numeroPedido = numeroPedido
        self.faturas = []
    
    def adicionar_fatura(self, fatura):
        self.faturas.append(fatura)
    
    # Exibir todas as faturas no pedido
    def exibir_faturas(self):
        if not self.faturas:
            print("Nenhuma fatura no pedido.")
        else:
            print(f"\n--- Pedido {self.numeroPedido} ---")
            for i, invoice in enumerate(self.faturas, start=1):
                print(f"\nFatura {i}:")
                print(f"Número do Item: {invoice.get_numeroItem()}")
                print(f"Descrição: {invoice.get_descricaoItem()}")
                print(f"Quantidade: {invoice.get_quantidadeComprada()}")
                print(f"Preço Unitário: R${invoice.get_precoItem():.2f}")
                print(f"Valor Total da Fatura: R${invoice.calcularFatura():.2f}")
    
    # Calcular o valor total do pedido (somando todas as faturas)
    def calcular_total_pedido(self):
        total = sum(fatura.calcularFatura() for fatura in self.faturas)
        return total


def main():
    pedidos = [] 
    continuarCadastrandoPedidos = "Y"
    
    print("-" * 20, "CADASTRO DE PEDIDOS", "-" * 20, "\n\n")
    
    while continuarCadastrandoPedidos.upper() == "Y":
        numeroPedido = len(pedidos) + 1  
        pedido = Pedido(numeroPedido)  
        
        continuarCadastrandoFaturas = "Y"
        
        while continuarCadastrandoFaturas.upper() == "Y":
            numItem = int(input("\nDigite o número do item: "))
            descricao = input("Digite a descrição do item: ")
            quantidade = int(input("Digite a quantidade comprada do item: "))
            preco = float(input("Digite o preço unitário do item: R$ "))

            invoiceProduct = Invoice(numItem, descricao, quantidade, preco)
            pedido.adicionar_fatura(invoiceProduct) 

            continuarCadastrandoFaturas = input("\nDeseja cadastrar outro produto neste pedido? (Y/n): ")

        pedidos.append(pedido)  
        
        continuarCadastrandoPedidos = input("\nDeseja cadastrar outro pedido? (Y/n): ")
    
    print("\n--- RESUMO DOS PEDIDOS ---")
    totalGeral = 0 
    
    for pedido in pedidos:
        pedido.exibir_faturas()
        totalPedido = pedido.calcular_total_pedido()
        print(f"\nValor Total do Pedido {pedido.numeroPedido}: R${totalPedido:.2f}")
        totalGeral += totalPedido 
    
    print(f"\nValor Total de Todos os Pedidos: R${totalGeral:.2f}")

main()
