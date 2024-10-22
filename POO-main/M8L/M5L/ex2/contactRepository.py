class ContactRepository:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, tel):
        contact = {'name': name, 'tel': tel}
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

    def edit_contact(self, name, tel):
        for contact in self.contacts:
            if contact['name'] == name or contact['tel'] == tel:
                new_name = input("Enter new name: ")
                new_tel = input("Enter new phone number: ")
                contact['name'] = new_name
                contact['tel'] = new_tel
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def remove_contact(self, name, tel):
        for contact in self.contacts:
            if contact['name'] == name or contact['tel'] == tel:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found!")

    def find_contact(self, name=None, tel=None):
        results = []
        for contact in self.contacts:
            if (name and contact['name'] == name) or (tel and contact['tel'] == tel):
                results.append(contact)
        return results

    def has_contacts(self):
        return len(self.contacts) > 0


class PhoneValidator:
    def validate(self, tel):
        # Simples validação de número de telefone (exemplo)
        if len(tel) == 11 and tel.isdigit():
            return True
        return False