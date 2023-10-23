# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print()

# Function to search for a contact
def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term == details["Phone"]:
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Current Details:")
        view_single_contact(name)
        phone = input("Enter the new phone number (press Enter to keep current): ")
        email = input("Enter the new email address (press Enter to keep current): ")
        address = input("Enter the new address (press Enter to keep current): ")
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        if address:
            contacts[name]["Address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Function to view a single contact
def view_single_contact(name):
    details = contacts[name]
    print(f"Name: {name}")
    print(f"Phone: {details['Phone']}")
    print(f"Email: {details['Email']}")
    print(f"Address: {details['Address']}")
    print()

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
