from date import Date
from event import Event

def main():
    while True:
        try:
            
            nome_evento = input("Insira o nome do evento: ")

            # Instanciando a classe Date
            dia_inicial = int(input("Insira o dia inicial: "))
            mes_inicial = int(input("Insira o mês inicial: "))
            ano_inicial = int(input("Insira o ano inicial: "))
            
            date = Date(dia_inicial, mes_inicial, ano_inicial)
            evento = Event(nome_evento, date)  # Associa o evento à nova data
            print(f"\nData inicial do evento '{evento.getNome()}':", date)

            # Alterando a data
            date.setDia(int(input("\nInsira o novo dia do evento: ")))
            date.setMes(int(input("Insira o novo mês do evento: ")))
            date.setAno(int(input("Insira o novo ano do evento: ")))
            # Testando a classe Event
            print()
            print(evento)
            break
        except ValueError:
            print("Insira valores válidos.")
    

main()