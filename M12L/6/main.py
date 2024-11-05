'''6. Implementar as classes do seguinte diagrama:
Detalhes:
• Atributo contacts[] é do tipo string e corresponde a uma lista de 3 posições.
• Atributo tax corresponde a uma porcentagem que será diminuída sobre o
paymentValue (10% para PF e 20% para PJ: estes valores devem ser
inicializados no construtor da classe).
• O método doPayment retorna o valor do pagamento diminuído da
porcentagem do imposto.'''
from legalPerson import LegalPerson
from physicalPerson import PhysicalPerson
from person import Person

def menu():
    print("1. Registrar pesosa física")
    print("2. Registrar pesosa jurídica")
    print("3. Vizualizar pessoa física")
    print("4. Vizualizar pessoa jurídica")
    print("0. Sair")
    print()
    option = input("Escolha uma opção: ")
    return option

def floatVerify(msg):
    try:
        number = float(input(msg))
        return number
    except ValueError:
        print("Valor inválido")
        return floatVerify(msg)

def registerPerson():
    name = input("Nome: ")
    address = input("Endereço: ")
    totalPayment= floatVerify("Salário Bruto: ")
    contacts = [input(f"Contato {i}: ") for i in range(3)]

    return name, address, totalPayment, contacts, Person(name, address, totalPayment, contacts)

def registerCPF():
    name, address, totalPayment, contacts, person = registerPerson()
    cpf = input("CPF: ")
    return PhysicalPerson(name, address, totalPayment, contacts, cpf), person

def registerCNPJ():
    name, address, totalPayment, contacts, person = registerPerson()
    cnpj = input("CNPJ: ")
    fantasyName = input("Nome fantasia: ")
    socialReason = input("Razão social: ")
    return LegalPerson(name, address, totalPayment, contacts, cnpj, fantasyName, socialReason), person

def main():

    while True:
        print("-"*60)
        option = menu()
        print("-"*60)
        if option == "1":
            newCPF, newPerson1 = registerCPF()
        elif option == "2":
            newCNPJ, newPerson2 = registerCNPJ()
        elif option == "3":
            newPerson1.showPersonalInfos()
            newCPF.showPersonalInfos()
        elif option == "4":
            newPerson2.showPersonalInfos()
            newCNPJ.showPersonalInfos()
        elif option == "0":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")

main()