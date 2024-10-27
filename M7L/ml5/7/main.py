'''Crie uma classe chamada Calendar que represente um calendário anual. Essa classe
deve ter métodos para exibir o calendário de um determinado mês, verificar se uma
data é feriado e calcular a diferença de dias entre duas datas.'''
from calendar_obj import Calendar
from br_holidays import BrHolidays
from us_holidays import UsHolidays

def main():
    year = int(input("Digite o ano: "))
    calendar = Calendar(year)

    while True:
        option = menu()

        try:
            if option == 1:
                month = int(input("Digite o mês: "))
                calendar.month.show(month)
            elif option == 2:
                region = input('Deseja verificar os feriados do Brasil ou do EUA? (BR/ EUA)')
                day = int(input("Digite o dia: "))
                month = int(input("Digite o mês: "))

                function = BrHolidays.verifyHoliday if region == 'BR' else UsHolidays.verifyHoliday
                print(calendar.verifyHoliday(day, month, function))
            elif option == 3:
                date1 = input("Digite a primeira data (dd-mm): ")
                date2 = input("Digite a segunda data (dd-mm): ")
                print(f"A diferença de dias entre as datas é de {calendar.calculate_days_between(date1, date2)} dias.")
            elif option == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except:
            print('Entrada inválida')

def menu():
    print("1 - Exibir calendário")
    print("2 - Verificar se é feriado")
    print("3 - Calcular diferença de dias")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

if __name__ == "__main__":
    main()