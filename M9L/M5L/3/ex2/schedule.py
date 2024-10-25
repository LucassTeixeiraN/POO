from contact import Contact
class Schedule:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, tel):
        if not self.validate_phone(tel):
            print("Invalid phone number.")
            return
        for contact in self.contacts:
            if contact.tel == tel:
                print("Contact already exists!")
                return
        contact = Contact(name, tel)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

    def edit_contact(self, name, tel):
        for contact in self.contacts:
            if contact.name == name or contact.tel == tel:
                new_name = input("Enter new name: ")
                new_tel = input("Enter new phone number: ")
                if not self.validate_phone(new_tel):
                    print("Invalid phone number.")
                    return
                contact.update(new_name, new_tel)
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def remove_contact(self, name=None, tel=None):
        for contact in self.contacts:
            if (name and contact.name == name) or (tel and contact.tel == tel):
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found!")

    def find_contact(self, name=None, tel=None):
        results = []
        for contact in self.contacts:
            if (name and contact.name == name) or (tel and contact.tel == tel):
                results.append(contact)
        return results

    @staticmethod
    def validate_phone(tel):
        # Simples validação de número de telefone (exemplo)
        return len(tel) == 11 and tel.isdigit()
