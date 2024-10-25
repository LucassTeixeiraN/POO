
from schedule import Schedule
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
                    tel = input("Enter phone number (DDD+9digits): ")
                    schedule.add_contact(name, tel)
                elif choice == 2:
                    schedule.view_contacts()
                elif choice == 3:
                    name = input("Enter name to edit: ")
                    tel = input("Enter phone number (DDD+9digits) to edit: ")
                    schedule.edit_contact(name, tel)
                elif choice == 4:
                    name = input("Enter name to remove: ")
                    tel = input("Enter phone number to remove: ")
                    schedule.remove_contact(name, tel)
                elif choice == 5:
                    name = input("Enter name to search: ")
                    tel = input("Enter phone number to search: ")
                    results = schedule.find_contact(name, tel)
                    if results:
                        for contact in results:
                            print(contact)
                    else:
                        print("Contact not found!")
                elif choice == 6:
                    print("Leaving...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid arguments")
main()

'''
+----------------+       +----------------+
|   Schedule     |<----->|    Contact     |
|----------------|       |----------------|
| - contacts     |       | - name         |
| + add_contact()|       | - tel          |
| + view_contacts()|     | + update()     |
| + edit_contact()|      | + __str__()    |
| + remove_contact()|    |                |
| + find_contact()|      |                |
+----------------+       +----------------+
'''