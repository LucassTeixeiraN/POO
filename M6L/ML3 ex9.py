'''Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.'''
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento}"


class Date:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def getDia(self):
        return self.dia
    
    def setDia(self, dia):
        self.dia = dia

    def getMes(self):
        return self.mes
    
    def setMes(self, mes):
        self.mes = mes

    def getAno(self):
        return self.ano
    
    def setAno(self, ano):
        self.ano = ano
    
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


def calcIdade(data_nascimento, dia_atual, mes_atual, ano_atual):
    anos = ano_atual - data_nascimento.getAno()
    if mes_atual < data_nascimento.getMes():
        anos -= 1
    elif mes_atual == data_nascimento.getMes() and dia_atual < data_nascimento.getDia():
        anos -= 1
    return anos


def main():
    nome = input("Insira o nome da pessoa: ")
    dia_nascimento = int(input("Insira o dia de nascimento: "))
    mes_nascimento = int(input("Insira o mês de nascimento: "))
    ano_nascimento = int(input("Insira o ano de nascimento: "))
    data_nascimento = Date(dia_nascimento, mes_nascimento, ano_nascimento)
    pessoa = Pessoa(nome, data_nascimento)

    dia_atual = int(input("Insira o dia atual: "))
    mes_atual = int(input("Insira o mês atual: "))
    ano_atual = int(input("Insira o ano atual: "))

    idade = calcIdade(data_nascimento, dia_atual, mes_atual, ano_atual)
    print(pessoa)
    print(f"A idade de {nome} é {idade} anos.")


main()
