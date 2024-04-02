class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print("Name:", contact.name)
            print("Phone Number:", contact.phone_number)
            print("Email:", contact.email)
            print("")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Name:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email:", contact.email)
                return
        print("Contact not found.")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "joyriya" and password == "joyriya":
        return True
    else:
        print("Invalid username or password.")
        return False

def main():
    if not login():
        return

    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()