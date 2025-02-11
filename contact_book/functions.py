def save_contact_details(contacts, name, phonenumber):
    """This function is independent, it is called in name_and_phonenumber function
    the number and name has to be validated before been saved calling this function"""
    contacts[name] = phonenumber
    print(f"{name}'s contact is saved successfully ✅")

def view_contacts(contacts):
    """print out the each contact (name and phone) if contact is not empty else return a ,essage to the user"""
    if not contacts:
        print("Your contact list is empty!")
        return
    for name, number in contacts.items():
        print(f"{name} - {number}")
    print(len(contacts.keys()), "contact(s) saved in list.")
    return True

def name_and_phonenum(contacts):
    """Validate phone number, name, and makes sure no duplicate allowed, then save."""
    while True:
        phonenumber = input("Enter phone number between 0-9: ")
        if phonenumber.isdigit() and len(phonenumber) == 11:
            if phonenumber in contacts.values():
                number_exist = [key for key, value in contacts.items() if value == phonenumber]
                print(f"{phonenumber} already exist with the name {number_exist[0]}", "\033[91mERROR\033[0m")
                return
            name = input("Save number with name: ").capitalize().strip()
            if not name:
                print("Name cannot be empty!", "\033[91mERROR\033[0m")
                return
            if name in contacts.keys():
                name_exist = [p for n, p in contacts.items() if n == name]
                print(f"{name} already exist with the number {name_exist[0]}", "\033[91mERROR\033[0m")
                return
            save_contact_details(contacts, name, phonenumber)
            return True
                    
        else:
            print("Only numbers are allowed and must be 11 digits", "\033[91mERROR\033[0m")
            continue       

def search_contact_by_phonenumber(contacts, phone_num):
    """Allows user to search for contact by phonenumber."""
    confirmed = False    
    if phone_num.isdigit():
        for name, number in contacts.items():
            if phone_num in number:
                print(name, number)
                confirmed = True
        if not confirmed:
            print(f"{phone_num} not found in any contact", "\033[91mERROR\033[0m")
            return
    else:
        print("Only numbers are allowed!", "\033[91mERROR\033[0m")
        return

def search_contact_by_name(contacts, name):
    """Allows user to search for contact by name."""
    confirmed = False
    name_search = name.strip()
    for x_name in contacts.keys():
        if name_search.lower() in x_name or name_search.capitalize() in x_name:
            print(x_name, contacts[x_name])
            confirmed = True
    if not confirmed:
        print(f"{name_search} not found in any contact", "\033[91mERROR\033[0m")
        return

def delete_contact(contacts, name):
    """Allows user to delete contact only by name"""
    if not contacts:
        return
    if name.capitalize().strip() not in contacts.keys():
        print(name, "not found in contact list", "\033[91mERROR\033[0m")
        return 
    del contacts[name.capitalize().strip()]
    print(name, "deleted from contact list successfully ✅")
            
def display_options():
    """Prints the options before and after each execution"""
    print()
    print(1, "to save contact")
    print(2, "to view contacts")
    print(3, "to search contacts")
    print(4, "to delete contact")
    print(5, "to exit")
    print()

