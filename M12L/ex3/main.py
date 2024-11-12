'''Crie uma classe chamada Ticket que possui um valor em reais e um método que
retorne o valor do ingresso.
    a. Crie uma classe VIP, que herda Ticket e possui um valor adicional. Crie um
método sobreposto que retorne o valor do ingresso VIP (com o adicional
incluído).
    b. Crie uma classe Normal, que herda Ticket e possui um método que retorna o
valor “normal” do ingresso.
    c. Crie uma classe LowerStateroom (que possui a localização do ingresso e
métodos para acessar e imprimir a localização) e uma classe
SuperiorStateroom, que é mais cara (possui valor adicional). Esta última
possui um método para retornar o valor do ingresso, sobrepondo o método
que retorna este valor. Ambas as classes herdam a classe VIP.'''
from ticket import Normal, VIP
from stateroom import LowerStateRoom, SuperiorStateRoom

def menu():
    print("\n--- Menu de Ingressos ---")
    print("1. Ingresso Normal")
    print("2. Ingresso VIP")
    print("3. Ingresso LowerStateroom")
    print("4. Ingresso SuperiorStateroom")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def main():
    while True:
        option = menu()
        
        if option == '1':
            price = float(input("Digite o valor do ingresso Normal: R$"))
            normal_ticket = Normal(price)
            
            print(f"Valor do ingresso Normal: R${normal_ticket.getValue()}")
        
        elif option == '2':
            price = float(input("Digite o valor do ingresso VIP: R$"))
            additional_fee = float(input("Digite o adicional para VIP: R$"))
            vip_ticket = VIP(price, additional_fee)

            print(f"Valor do ingresso VIP: R${vip_ticket.getValue()}")
        
        elif option == '3':
            price = float(input("Digite o valor do ingresso LowerStateroom: R$"))
            additional_fee = float(input("Digite o adicional para VIP: R$"))
            location = input("Digite a localização do ingresso LowerStateroom: ")
            lower_ticket = LowerStateRoom(price, additional_fee, location)

            print(f"Valor do ingresso LowerStateroom: R${lower_ticket.getValue()}")
            lower_ticket.printLocation()
        
        elif option == '4':
            price = float(input("Digite o valor do ingresso SuperiorStateroom: R$"))
            additional_fee = float(input("Digite o adicional para VIP: R$"))
            superior_fee = float(input("Digite o adicional superior para SuperiorStateroom: R$"))
            location = input("Digite a localização do ingresso SuperiorStateroom: ")
            superior_ticket = SuperiorStateRoom(price, additional_fee, location, superior_fee)

            print(f"Valor do ingresso SuperiorStateroom: R${superior_ticket.getValue()}")
            superior_ticket.printLocation()
        
        elif option == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()