from functions import name_and_phonenum, view_contacts, display_options, search_contact_by_phonenumber, search_contact_by_name, delete_contact

contacts = {}   
while True:
    display_options()
    try:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                name_and_phonenum(contacts)
            case 2:
                view_contacts(contacts)
            case 3:
                if not contacts:
                    print(" ⚠️ Your contact list is empty")
                    continue
                num_or_name = input("Enter 'p' for number, or 'n' for name to search contact: ").lower().strip()
                if num_or_name == 'p':
                    phonenumber = input("Enter phone number between 0-9: ")
                    search_contact_by_phonenumber(contacts, phonenumber)
                elif num_or_name == 'n':
                    name = input("Enter name: ")
                    search_contact_by_name(contacts, name)
                else:
                    print("⚠️ Invalid input")
            case 4:
                name = input("Type contact name to delete: ")
                delete_contact(contacts, name)
            case 5:
                print("Bye!")
                break
            case _:
                print("⚠️ Invalid input, try again!")

    except ValueError:
        print("Only numbers are allowed!")
