'''Implemente uma classe chamada Schedule que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.'''

class Schedule:
    def __init__(self):
        self.contacts = []

    def addContact(self, name, tel):
        contact = {'name': name, 'tel': tel}
        self.contacts.append(contact)

    def viewListContacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Tel: {contact['tel']}")

    def editContact(self, name, tel):
        for contact in self.contacts:
            if contact['name'] == name or contact['tel'] == tel:
                new_name = input("Enter new name: ")
                new_tel = input("Enter new phone number: ")
                contact['name'] = new_name
                contact['tel'] = new_tel
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def removeContact(self, name, tel):
        for contact in self.contacts:
            if contact['name'] == name or contact['tel'] == tel:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found!")

    def findContact(self, name=None, tel=None):
        results = []
        for contact in self.contacts:
            if (name and contact['name'] == name) or (tel and contact['tel'] == tel):
                results.append(contact)
        return results
    
def menu():
    print("Phonebook Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Remove Contact")
    print("5. Search Contact")
    print("6. Quit")
    options = int(input("Digite sua opção: "))
    if options < 1 or options > 6:
        print("Opção inválida\n")
    return options

def main():
    schedule = Schedule()
    while True:
        try:
            if input("Press ENTER to go to the MENU.") == '':
                choice = menu()
                if choice == 1:
                    name = input("Enter name: ")
                    tel = input("Enter phone number: ")
                    schedule.addContact(name, tel)
                elif choice == 2:
                    schedule.viewListContacts()
                elif choice == 3:
                    name = input("Enter name or phone number to edit: ")
                    tel = input("Enter phone number to edit: ")
                    schedule.editContact(name, tel)
                elif choice == 4:
                    name = input("Enter name or phone number to remove: ").lower()
                    tel = input("Enter phone number to remove: ")
                    schedule.removeContact(name, tel)
                elif choice == 5:
                    name = input("Enter name to search: ").lower()
                    tel = input("Enter phone number to search: ")
                    results = schedule.findContact(name, tel)
                    if results:
                        for contact in results:
                            print(f"Name: {contact['name']}, Tel: {contact['tel']}")
                    else:
                        print("Contact not found!")
                elif choice == 6:
                    print("Leaving...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except(ValueError):
            print("Invalid arguments")
main()    