class Event:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data  # data é uma instância da classe Date

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def __str__(self):
        return f"Nova data do evento '{self.nome}': {self.data}"
