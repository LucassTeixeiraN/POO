class TipoProduto:
    def __init__(self, nome, taxa_imposto):
        self.nome = nome
        self.taxa_imposto = taxa_imposto

    def calcular_imposto(self, fatura):
        return fatura * self.taxa_imposto

class Invoice:
    def __init__(self, numItem, descricao, quantidade, preco, tipo_produto: TipoProduto):
        self.__numeroItem = numItem
        self.__descricaoItem = descricao
        
        self.__quantidadeComprada = max(0, quantidade)
        self.__precoItem = max(0, preco)
        
        if not isinstance(tipo_produto, TipoProduto):
            raise ValueError("tipo_produto deve ser uma instância de TipoProduto")
        self.__tipo_produto = tipo_produto

    def calcular_fatura(self):
        return self.__quantidadeComprada * self.__precoItem
    
    def calcular_imposto(self):
        return self.__tipo_produto.calcular_imposto(self.calcular_fatura())

def main():
    produtos = []
    continuar_cadastrando = "S"
    print("-" * 20, "CADASTRO DE ITENS", "-" * 20, "\n")

    tipos_produto = {
        1: TipoProduto("Periférico", 1.25),
        2: TipoProduto("Peça de Hardware", 1.13),
        3: TipoProduto("Equipamento de Áudio", 1.05),
        4: TipoProduto("IoT", 1.20),
        5: TipoProduto("Outro (genérico)", 1.10),
    }

    while continuar_cadastrando.upper() == "S":
        numItem = int(input("\nDigite o número do item: "))
        descricao = input("Digite a descrição do item: ")
        quantidade = int(input("Digite a quantidade comprada do item: "))
        preco = float(input("Digite o preço unitário do item: R$ "))

        print("\nEscolha o tipo de produto:")
        for k, v in tipos_produto.items():
            print(f"{k} - {v.nome} (Taxa de Imposto: {v.taxa_imposto:.2f})")

        tipo = int(input("Digite o número correspondente ao tipo de produto: "))
        
        if tipo < 1 or tipo > 5:
            print("Tipo inválido. Usando tipo genérico.")
            tipo_produto = tipos_produto[5]
        else:
            tipo_produto = tipos_produto[tipo]

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
