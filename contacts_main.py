# Denne funktion gør to ting:
# * Viser en menu med valgmuligheder
# * Beder brugeren indtaste et tal, som
#   skal angive en af disse valgmuligheder.
#   Det indtastede tal returneres.
def menu():
    print("0: Quit")
    print("1: Show contacts")
    print("2: Show contact details")
    print("3: Add contact")
    print("4: Delete contact")
    print("5: Add number to contact")

    inp = input("> ")
    while not inp.isnumeric():
        inp = input("> ")
    
    return int(inp)

# Viser kontakternes navne, sorteret alfabetisk.
def show_contacts():
    print("CONTACTS")
    print("----------------")
    names = list(contacts.keys())
    names.sort()
    for name in names:
        print(name)
    print("----------------")

# Viser telefonnummer for den angivne kontakt.
def show_details(name):
    print("----------------")
    if name in contacts:
        print(name)
        print(contacts[name])
    else:
        print("Not found.")
    print("----------------")

def add_contact():
    newName = input("Name?")
    newNum = input("Number?")
    if(len(newName) != 0 and len(newNum) != 0 and newName not in contacts):
        contacts[newName] = [newNum]
    elif(newName in contacts):
        print("Such a name already exists in the contacts!")
    else:
        print("The name or the number are not filled!")

def del_contact(): # Slet kontakt funktion
    deleteContact = input("Which contact do you want to delete?\n > ") # Brugeren indtaster selve navnet
    if deleteContact in contacts: 
        del contacts[deleteContact] # Den fjerner quite literally vores value ved bare at tage den string vi inputter i vores "deleteContact" input line
        print(f"{deleteContact} has been deleted.") # "f" i vores print er fordi ellers kan vi ikke få {deleteContact} med 
    else:
        print(f"Contact '{deleteContact}' not found.") # "f" i vores print er fordi ellers kan vi ikke få {deleteContact} med

def add_num_to_contact():
    addName = input("Who to add number to? name> ")
    addNum = input("Number to add number> ")

    if(addName in contacts):
        contacts[addName].append(addNum)
    else:
        print("Such a person was not found in the contacts!")
    

contacts = {
    "Isakohackeren" : ["31975613"],
    "Eugen" : ["53641082"],
    "Noah Alexander Den 1" : ["30551533"]
}

while True:
    print()
    inp = menu()
    print()

    if inp == 0:
        break

    elif inp == 1:
        show_contacts()

    elif inp == 2:
        name = input("Enter name: ")
        show_details(name)
    elif inp == 3: #add contact 
        add_contact()
    elif inp == 4: #delete contact
        del_contact()
    elif inp == 5: #add number to existing contact
        add_num_to_contact()
