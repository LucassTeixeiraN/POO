class TipoProduto:
    def __init__(self, taxa_imposto):
        self.taxa_imposto = taxa_imposto

    def calcular_imposto(self, fatura):
        return fatura * self.taxa_imposto

class Invoice:
    def __init__(self, numItem, descricao, quantidade, preco, tipo_produto):
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
            
        self.tipo_produto = tipo_produto

    @staticmethod
    def verif_maior_zero(num):
        return num > 0

    def calcular_fatura(self):
        return self.__quantidadeComprada * self.__precoItem
    
    def calcular_imposto(self):
        return self.tipo_produto.calcular_imposto(self.calcular_fatura())

def main():
    produtos = []
    continuar_cadastrando = "S"
    print("-" * 20, "CADASTRO DE ITENS", "-" * 20, "\n")

    tipos_produto = {
        1: TipoProduto(1.25),  # Periférico
        2: TipoProduto(1.13),  # Peça de Hardware
        3: TipoProduto(1.05),  # Equipamento de Áudio
        4: TipoProduto(1.20),  # IoT
        5: TipoProduto(1.10),  # Outro (genérico)
    }

    while continuar_cadastrando.upper() == "S":
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
            
        tipo_produto = tipos_produto.get(tipo, tipos_produto[5])  # Usa genérico se tipo inválido

        # Cria Invoice com injeção de dependência
        produto = Invoice(numItem, descricao, quantidade, preco, tipo_produto)
        produtos.append(produto)

        continuar_cadastrando = input("\nDeseja cadastrar outro produto? (S/n): ")

    print("\nFaturas cadastradas: ")
    for i, invoice in enumerate(produtos, start=1):
        print(f"\nFatura {i}:")
        print(f"Número do Item: {invoice._Invoice__numeroItem}")
        print(f"Descrição: {invoice._Invoice__descricaoItem}")
        print(f"Quantidade: {invoice._Invoice__quantidadeComprada}")
        print(f"Preço Unitário: R${invoice._Invoice__precoItem:.2f}")
        print(f"Valor Total da Fatura: R${invoice.calcular_fatura():.2f}")
        print(f"Valor Total com Imposto: R${invoice.calcular_imposto():.2f}")


main()
