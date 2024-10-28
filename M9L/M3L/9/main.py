from date import Date
from event import Event

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
