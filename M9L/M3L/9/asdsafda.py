class Date:
    def __init__(self, dia, mes, ano, evento=None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.evento = evento  

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
    
    def getEvento(self):
        return self.evento
    
    def setEvento(self, evento):
        self.evento = evento

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    

class Event:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        data.setEvento(self) 

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
        data.setEvento(self)  

    def __str__(self):
        return f"Nova data do evento '{self.nome}': {self.data}"   
    

def main():
    while True:
        try:
            nome_evento = input("Insira o nome do evento: ")

            dia_inicial = int(input("Insira o dia inicial: "))
            mes_inicial = int(input("Insira o mês inicial: "))
            ano_inicial = int(input("Insira o ano inicial: "))
            
            date = Date(dia_inicial, mes_inicial, ano_inicial)
            evento = Event(nome_evento, date) 
            print(f"\nData inicial do evento '{evento.getNome()}':", date)

         
            date.setDia(int(input("\nInsira o novo dia do evento: ")))
            date.setMes(int(input("Insira o novo mês do evento: ")))
            date.setAno(int(input("Insira o novo ano do evento: ")))

        
            print()
            print(evento)
            print("Evento associado à data:", date.getEvento().getNome())
            break
        except ValueError:
            print("Insira valores válidos.")
    

main()
