import pickle
import os
PATH = "C:/Users/Zanis/Desktop/Python Docs/Step1-Python/20-project(library)/"

def check_file_exist():
    import os
    if not os.path.exists(PATH+"users.dat") :
        f = open(PATH+"users.dat", 'wb')
        users_dict = {}
        pickle.dump(users_dict, f)
    
    if not os.path.exists(PATH+"books.dat") :
        f = open(PATH+"books.dat", 'wb')
        books_dict = {}
        pickle.dump(books_dict, f)

    if not os.path.exists(PATH+"borrows.dat") :
        f = open(PATH+"borrows.dat", 'wb')
        borrows_dict = {}
        pickle.dump(borrows_dict, f)

        

def add_user(name, family, father_name, code, birthday):
    check_file_exist()

    f = open(PATH+'users.dat', 'rb')
    users_dict = pickle.load(f)
    f.close()
    user_id = len(users_dict)
    users_dict[user_id] = [name, family, father_name, code, birthday]

    f = open(PATH+'users.dat', 'wb')
    pickle.dump(users_dict, f)
    f.close()
    print("user added successfuly with library code : " , user_id)



def add_book(title, author, subject, year):
    check_file_exist()
    f = open(PATH+'books.dat', 'rb')
    book_dict = pickle.load(f)
    f.close()
    book_dict[title] = [author, subject, year]

    f = open(PATH+'books.dat', 'wb')
    pickle.dump(book_dict, f)
    f.close()


def search_book(title):
    f = open(PATH+'books.dat', 'rb')
    book_dict = pickle.load(f)
    f.close()
    print(book_dict[title])


def borrow(user_id, title):
    check_file_exist()
    f = open(PATH+'borrows.dat', 'rb')
    borrows_dict = pickle.load(f)
    f.close()
    borrows_dict[user_id] = title

    f = open(PATH+'borrows.dat', 'wb')
    pickle.dump(borrows_dict, f)
    f.close()

def show_all_info():
    f = open(PATH+'users.dat', 'rb')
    users_dict = pickle.load(f)
    f.close()
    f = open(PATH+'books.dat', 'rb')
    books_dict = pickle.load(f)
    f.close()
    f = open(PATH+'borrows.dat', 'rb')
    borrows_dict = pickle.load(f)
    f.close()

    print(users_dict)
    print("-------------------------------------------------")
    print(books_dict)
    print("-------------------------------------------------")
    print(borrows_dict)
    print("-------------------------------------------------")



ch = 1
while ch != 0:
    print("1-Add User\n2-Add new Book\n3-Search book\n4-Borrow\n5-Show All info\n0-Exit")
    ch = int(input("Enter Choice:"))
    os.system("cls")
    
    if ch == 1:
        name = input('Enter Name:')
        family = input('Enter Family:')
        father_name = input('Enter Father:')
        code = input('Enter Nationality Code:')
        birthday = input('Enter Birthday:')
        add_user(name, family, father_name, code, birthday)

    elif ch == 2:
        title = input('Enter Title:')
        author = input('Enter Author:')
        subject = input('Enter Subject:')
        year = input('Enter year:')
        add_book(title, author, subject, year)

    elif ch == 3:
        book_title = input('Enter Book Title:')
        search_book(book_title)

    elif ch == 4:
        user_id = input('Enter User id :')
        title = input('Enter Title:')
        borrow(user_id, title)

    elif ch == 5:
        show_all_info()