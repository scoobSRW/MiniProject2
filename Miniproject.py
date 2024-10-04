import re
import json

contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")


def validate_phone(phone):
    pattern = re.compile(r"^\d{10}$")
    return pattern.match(phone)


def validate_email(email):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    return pattern.match(email)


def add_contact():
    try:
        phone = input("Enter phone number (10 digits): ")
        if not validate_phone(phone):
            raise ValueError("Invalid phone number format.")

        if phone in contacts:
            raise ValueError("Contact already exists with this phone number.")

        name = input("Enter name: ")
        email = input("Enter email address: ")
        if not validate_email(email):
            raise ValueError("Invalid email format.")

        additional_info = input("Enter additional information (optional): ")

        contacts[phone] = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Additional Info': additional_info
        }
        print(f"Contact {name} added successfully.")
    except ValueError as e:
        print(e)

def edit_contact():
    try:
        phone = input("Enter phone number of the contact to edit: ")
        if phone not in contacts:
            raise KeyError("Contact not found.")

        name = input("Enter new name (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        if email and not validate_email(email):
            raise ValueError("Invalid email format.")

        additional_info = input("Enter new additional information (optional): ")

        if name:
            contacts[phone]['Name'] = name
        if email:
            contacts[phone]['Email'] = email
        if additional_info:
            contacts[phone]['Additional Info'] = additional_info

        print("Contact updated successfully.")
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)

def delete_contact():
    try:
        phone = input("Enter phone number of the contact to delete: ")
        if phone not in contacts:
            raise KeyError("Contact not found.")

        del contacts[phone]
        print("Contact deleted successfully.")
    except KeyError as e:
        print(e)


def search_contact():
    phone = input("Enter phone number to search: ")
    contact = contacts.get(phone)
    if contact:
        print(json.dumps(contact, indent=4))
    else:
        print("Contact not found.")


def display_all_contacts():
    if contacts:
        for contact in contacts.values():
            print(json.dumps(contact, indent=4))
    else:
        print("No contacts to display.")


def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            json.dump(contacts, file, indent=4)
        print("Contacts exported to contacts.txt.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("contacts.txt not found.")
    except Exception as e:
        print(f"Error importing contacts: {e}")


# Main loop
def main():
    while True:
        display_menu()
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
