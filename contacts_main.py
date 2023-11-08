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

contacts = {
    "Cecilia" : "31975613",
    "Alice" : "12345678",
    "Bob" : "23456789"
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

    elif inp == 3:
        print("NOT IMPLEMENTED YET")
    elif inp == 4: # Delete contact
        print("NOT IMPLEMENTED YET")
    elif inp == 5:
        print("NOT IMPLEMENTED YETti")
