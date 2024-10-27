
class Schedule:
    def __init__(self, contact_repository, phone_validator):
        self.contact_repository = contact_repository
        self.phone_validator = phone_validator

    def add_contact(self, name, tel):
        if not self.phone_validator.validate(tel):
            print("Invalid phone number.")
            return
        self.contact_repository.add_contact(name, tel)
        print("Contact added successfully!")

    def view_contacts(self):
        contacts = self.contact_repository.get_contacts()
        for contact in contacts:
            print(f"Name: {contact['name']}, Tel: {contact['tel']}")

    def edit_contact(self, name, tel):
        self.contact_repository.edit_contact(name, tel)

    def remove_contact(self, name, tel):
        self.contact_repository.remove_contact(name, tel)

    def find_contact(self, name=None, tel=None):
        return self.contact_repository.find_contact(name, tel)
