'''Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.'''

class Date():
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
        return (f"{self.dia}/{self.mes}/{self.ano}")

def main():
    date = Date(10, 11, 2004)

    print(f"HOJE: {date.getDia()}/{date.getMes()}/{date.getAno()}\n")

    date.setDia(int(input("Insira o novo dia: ")))
    date.setMes(int(input("Insira o novo mes: ")))
    date.setAno(int(input("Insira o novo ano: ")))

    print("\nNova data:", date)

main()