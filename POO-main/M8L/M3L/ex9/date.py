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

