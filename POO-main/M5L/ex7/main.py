'''Crie uma classe chamada Calendar que represente um calendário anual. Essa classe
deve ter métodos para exibir o calendário de um determinado mês, verificar se uma
data é feriado e calcular a diferença de dias entre duas datas.'''
from calendar_obj import Calendar

def main():
    calendar = Calendar(2024)

    calendar.showMonth(2)
    print(calendar.verifyHoliday(25, 10))

    diff_days = calendar.calculateDaysBetween("01-01-2024", "01-02-2024")
    print(f"A diferença de dias é: {diff_days}")

main()