import re

class ContactManager:
    def __init__(self):
        self.contacts = [
            (1, "Alice Nsubuga", "+256-700-123456", "alice@domain.com"),
            (2, "Bob Okello", "+256772111222", "bob.okello@company.org"),
            (3, "Charlie Mukasa", "+1-555-987-6543", "charlie.m@web.co")
        ]
        self.next_id = 4

    def validate_phone(self, phone):
        """Validates phone structure."""
        pattern = r"^\+[0-9-]+$"
        return bool(re.match(pattern, phone))

    def validate_email(self, email):
        """Validates email structure."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def print_table(self, results):
        """Helper method to format and display list of contact tuples cleanly."""
        if not results:
            print("\nNo contacts found.")
            return

        print("\n" + "=" * 65)
        print(f"{'ID':<5} | {'Name':<20} | {'Phone Number':<18} | {'Email':<20}")
        print("=" * 65)
        for contact in results:
            c_id, name, phone, email = contact
            print(f"{c_id:<5} | {name:<20} | {phone:<18} | {email:<20}")
        print("=" * 65)
        print(f"Total entries: {len(results)}\n")

    def add_contact(self, name, phone, email):
        """Creates and appends a new contact if validations pass."""
        if not name:
            print("Error: Name cannot be blank.")
            return
        if not self.validate_phone(phone):
            print("Error: Invalid phone format. Must start with '+' followed by digits/hyphens.")
            return
        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return

        new_contact = (self.next_id, name, phone, email)
        self.contacts.append(new_contact)
        self.next_id += 1
        print(f"Contact '{name}' added successfully with ID {new_contact[0]}.")

    def view_contact(self, contact_id):
        """Finds and displays a single contact by its unique ID."""
        for contact in self.contacts:
            if contact[0] == contact_id:
                self.print_table([contact])
                return
        print(f"Contact with ID {contact_id} not found.")

    def update_contact(self, contact_id, name, phone, email):
        """Updates contact fields. Keeps old values if new inputs are left blank."""
        for i, contact in enumerate(self.contacts):
            c_id, old_name, old_phone, old_email = contact
            if c_id == contact_id:
                new_name = name if name else old_name
                new_phone = phone if phone else old_phone
                new_email = email if email else old_email

                if new_phone != old_phone and not self.validate_phone(new_phone):
                    print("Error: Invalid phone format update rejected.")
                    return
                if new_email != old_email and not self.validate_email(new_email):
                    print("Error: Invalid email format update rejected.")
                    return

                self.contacts[i] = (contact_id, new_name, new_phone, new_email)
                print(f"Contact ID {contact_id} updated successfully.")
                return
        print(f"Contact with ID {contact_id} not found.")

    def delete_contact(self, contact_id):
        """Removes a contact from the list by ID."""
        for contact in self.contacts:
            if contact[0] == contact_id:
                self.contacts.remove(contact)
                print(f"Contact ID {contact_id} successfully deleted.")
                return
        print(f"Contact with ID {contact_id} not found.")

    def search_contacts(self, query):
        """Searches across name, phone, and email fields."""
        query = query.lower()
        matched = []
        for contact in self.contacts:
            _, name, phone, email = contact
            if query in name.lower() or query in phone.lower() or query in email.lower():
                matched.append(contact)
        self.print_table(matched)

    def list_all_contacts(self):
        """Displays all contacts currently in the system."""
        self.print_table(self.contacts)


def main():
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone (+XX-XXX-XXX): ").strip()
            email = input("Enter Email: ").strip()
            manager.add_contact(name, phone, email)

        elif choice == '2':
            try:
                contact_id = int(input("Enter Contact ID to view: ").strip())
                manager.view_contact(contact_id)
            except ValueError:
                print("Invalid input. ID must be an integer number.")

        elif choice == '3':
            try:
                contact_id = int(input("Enter Contact ID to update: ").strip())
                print("(Press Enter to leave a field unchanged)")
                name = input("Enter New Name: ").strip()
                phone = input("Enter New Phone: ").strip()
                email = input("Enter New Email: ").strip()
                manager.update_contact(contact_id, name, phone, email)
            except ValueError:
                print("Invalid input. ID must be an integer number.")

        elif choice == '4':
            try:
                contact_id = int(input("Enter Contact ID to delete: ").strip())
                manager.delete_contact(contact_id)
            except ValueError:
                print("Invalid input. ID must be an integer number.")

        elif choice == '5':
            query = input("Enter search keyword (Name/Phone/Email): ").strip()
            if query:
                manager.search_contacts(query)
            else:
                print("Search query cannot be blank.")

        elif choice == '6':
            manager.list_all_contacts()

        elif choice == '7':
            print("\nThanks for using Contact Manager.")
            break
            
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()

