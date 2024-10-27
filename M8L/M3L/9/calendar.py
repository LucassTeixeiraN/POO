class Calendar:
    def __init__(self):
        self.dates = []

    def add_date(self, date):
        self.dates.append(date)

    def display_dates(self):
        for date in self.dates:
            print(date)

    def update_date(self, index, dia, mes, ano):
        if 0 <= index < len(self.dates):
            self.dates[index].setDia(dia)
            self.dates[index].setMes(mes)
            self.dates[index].setAno(ano)
        else:
            print("Índice inválido.")
