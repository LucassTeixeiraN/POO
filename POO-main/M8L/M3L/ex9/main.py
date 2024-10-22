from calendar import Calendar
from date import Date
def main():
    # Criando instâncias de Date
    date1 = Date(10, 11, 2004)
    date2 = Date(25, 12, 2020)

    # Criando uma instância de Calendar e injetando as datas
    calendar = Calendar()
    calendar.add_date(date1)
    calendar.add_date(date2)

    print("Datas no calendário:")
    calendar.display_dates()

    # Atualizando uma data
    print("\nAtualizando a primeira data...")
    new_dia = int(input("Insira o novo dia: "))
    new_mes = int(input("Insira o novo mês: "))
    new_ano = int(input("Insira o novo ano: "))

    calendar.update_date(0, new_dia, new_mes, new_ano)

    print("\nAtualizando a segunda data...")
    new_dia = int(input("Insira o novo dia: "))
    new_mes = int(input("Insira o novo mês: "))
    new_ano = int(input("Insira o novo ano: "))

    calendar.update_date(1, new_dia, new_mes, new_ano)

    print("\nDatas atualizadas no calendário:")
    calendar.display_dates()

main()

# Injeção de Dependência: No método main, instâncias da classe Date são criadas e injetadas na classe Calendar usando o método add_date. Isso demonstra a injeção de dependência, onde a classe Calendar depende da classe Date para funcionar.

