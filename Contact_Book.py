import json
import os

# File to store the contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return [] # Return empty list if file is empty or corrupted

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    """Display the list of contacts."""
    if not contacts:
        print("\n📭 Your contact book is empty!")
        return
    
    print("\n" + "="*65)
    print(f"{'No.':<5} | {'Name':<20} | {'Phone Number':<15} | {'Email':<20}")
    print("-" * 65)
    for index, contact in enumerate(contacts, start=1):
        print(f"{index:<5} | {contact['name']:<20} | {contact['phone']:<15} | {contact['email']:<20}")
    print("="*65 + "\n")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact (by Name or Phone)")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        # 1. ADD CONTACT
        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()
            
            if name and phone: # Basic validation
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                })
                save_contacts(contacts)
                print(f"✅ Contact '{name}' added successfully!")
            else:
                print("❌ Name and Phone Number are required to add a contact.")
                
        # 2. VIEW CONTACTS
        elif choice == '2':
            display_contacts(contacts)
            
        # 3. SEARCH CONTACT
        elif choice == '3':
            query = input("Enter Name or Phone Number to search: ").strip().lower()
            found = False
            print("\n--- Search Results ---")
            for contact in contacts:
                if query in contact['name'].lower() or query in contact['phone']:
                    print(f"👤 Name: {contact['name']}")
                    print(f"   Phone: {contact['phone']}")
                    print(f"   Email: {contact['email']}")
                    print(f"   Address: {contact['address']}\n")
                    found = True
            
            if not found:
                print("❌ No contacts found matching your search.")

        # 4. UPDATE CONTACT
        elif choice == '4':
            display_contacts(contacts)
            if contacts:
                try:
                    index = int(input("Enter the 'No.' of the contact you want to update: ")) - 1
                    if 0 <= index < len(contacts):
                        contact = contacts[index]
                        print(f"\nUpdating {contact['name']} (Leave blank to keep current value)")
                        
                        new_name = input(f"New Name [{contact['name']}]: ").strip()
                        new_phone = input(f"New Phone [{contact['phone']}]: ").strip()
                        new_email = input(f"New Email [{contact['email']}]: ").strip()
                        new_address = input(f"New Address [{contact['address']}]: ").strip()
                        
                        if new_name: contact['name'] = new_name
                        if new_phone: contact['phone'] = new_phone
                        if new_email: contact['email'] = new_email
                        if new_address: contact['address'] = new_address
                        
                        save_contacts(contacts)
                        print("✅ Contact updated successfully!")
                    else:
                        print("❌ Invalid contact number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

        # 5. DELETE CONTACT
        elif choice == '5':
            display_contacts(contacts)
            if contacts:
                try:
                    index = int(input("Enter the 'No.' of the contact you want to delete: ")) - 1
                    if 0 <= index < len(contacts):
                        deleted = contacts.pop(index)
                        save_contacts(contacts)
                        print(f"🗑️ Deleted contact: {deleted['name']}")
                    else:
                        print("❌ Invalid contact number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
                    
        # 6. EXIT
        elif choice == '6':
            print("\n👋 Exiting Contact Book. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
