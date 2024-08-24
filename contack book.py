import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("\nNo matching contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print(f"\nUpdating contact '{contact['name']}':")
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            save_contacts(contacts)
            print(f"\nContact '{contact['name']}' updated successfully.")
            return
    print(f"\nContact with name '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"\nContact '{contact['name']}' deleted successfully.")
            return
    print(f"\nContact with name '{name}' not found.")

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
