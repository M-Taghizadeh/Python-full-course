import os
# if not os.path.exists(PATH) :
#     f = open(PATH, 'w+')
#     f.write("")

PATH = "C:/Users/Zanis/Desktop/Python Docs/Step1-Python/18-project(phonebook)/database.txt"

### Funcyions
def add(name, number):
    f = open(PATH, "a+")
    new_phone = name + ":" + number + "\n"
    f.write(new_phone)
    f.close()

    os.system('cls')

def search(name):
    f = open(PATH, 'r')
    for line in f.readlines():
        if name == line.split(":")[0]:
            print(name + ":" + line.split(":")[1])
    f.close()

def delete(name):
    f = open(PATH, 'r')
    new_database = ""
    for line in f.readlines():
        if not name == line.split(":")[0]:
            new_database += line
    f.close()

    f = open(PATH, 'w')
    f.write(new_database)
    f.close()

def show_all():
    f = open(PATH, 'r')
    docs = f.read()
    print(docs)
    f.close()


### MENU 
ch = 1
while ch != 0:
    print("1-Add new Phone\n2-Search Phone\n3-Delete a phone\n4-Show all documents\n0-Exit")
    ch = int(input('Enter Your Choice :'))
    os.system('cls')

    if ch == 1:
        name = input("Enter Name : ")
        number = input("Enter Phone Number :")
        add(name, number)

    elif ch == 2:
        name = input("Enter Name for search : ")
        search(name)       

    elif ch == 3:
        name = input("Enter Name for delete : ")
        delete(name)

    elif ch == 4:
        show_all()