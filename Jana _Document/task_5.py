class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if contact.name.lower() == query.lower() or contact.phone == query]
        if results:
            for contact in results:
                print(contact)
        else:
            print("Contact not found.")

    def update_contact(self, query):
        for contact in self.contacts:
            if contact.name.lower() == query.lower() or contact.phone == query:
                print("Current details:", contact)
                contact.name = input("Enter new name: ") or contact.name
                contact.phone = input("Enter new phone: ") or contact.phone
                contact.email = input("Enter new email: ") or contact.email
                contact.address = input("Enter new address: ") or contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if contact.name.lower() == query.lower() or contact.phone == query:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Options:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            query = input("Enter name or phone to update: ")
            contact_book.update_contact(query)
        elif choice == "5":
            query = input("Enter name or phone to delete: ")
            contact_book.delete_contact(query)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
