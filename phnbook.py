phone_book = {}

def add():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print(f"Added contact: {name} - {number}")

def search():
    name = input("Enter name to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} not found in the phone book.")

def delete():
    name = input("Enter name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Deleted contact: {name}")
    else:
        print(f"{name} not found in the phone book.")

while True:
    print("\nPhone Book Menu:")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add()
    elif choice == '2':
        search()
    elif choice == '3':
        delete()
    elif choice == '4':
        print("Exiting phone book.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")