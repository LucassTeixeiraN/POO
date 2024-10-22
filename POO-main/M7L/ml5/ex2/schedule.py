class Contact:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def __repr__(self):
        return f"Name: {self.name}, Tel: {self.tel}"

class PhoneValidator:
    @staticmethod
    def validate(tel):
        """Simple phone number validation"""
        return len(tel) == 11 and tel.isdigit()

class Schedule:
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        if not PhoneValidator.validate(contact.tel):
            print("Invalid phone number.")
            return
        for existing_contact in self.contacts:
            if existing_contact.tel == contact.tel:
                print("Contact already exists!")
                return
        self.contacts.append(contact)
        print("Contact added successfully!")

    def viewListContacts(self):
        for contact in self.contacts:
            print(contact)

    def editContact(self, name, tel):
        for contact in self.contacts:
            if contact.name == name or contact.tel == tel:
                new_name = input("Enter new name: ")
                new_tel = input("Enter new phone number: ")
                if not PhoneValidator.validate(new_tel):
                    print("Invalid phone number.")
                    return
                contact.name = new_name
                contact.tel = new_tel
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def removeContact(self, name, tel):
        for contact in self.contacts:
            if contact.name == name or contact.tel == tel:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found!")

    def findContact(self, name=None, tel=None):
        results = []
        for contact in self.contacts:
            if (name and contact.name == name) or (tel and contact.tel == tel):
                results.append(contact)
        return results

    @classmethod
    def from_list(cls, contacts_list):
        schedule = cls()
        for contact in contacts_list:
            schedule.addContact(Contact(contact['name'], contact['tel']))
        return schedule


'''Classe Contact: Cada contato agora é uma instância da classe Contact, que encapsula o nome e o telefone.

Classe PhoneValidator: Uma classe separada para validação de números de telefone, permitindo que novos métodos de validação sejam adicionados sem modificar a classe Schedule.

O método addContact aceita instâncias da classe Contact, permitindo que novos tipos de contatos sejam facilmente adicionados.'''