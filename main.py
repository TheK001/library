from services import *
from utils import *
def main_menu():
    while True:
        options = ['Login', 'Register', 'Eixit']
        options = ['Show all books', 'Add book', 'Update book', 'Delete book', ]
        print_menu(options)
        choice = user_choice(len(options))
        if choice == 1:
            login()

        if choice == 2:
            register()
        if choice == 3:
            break

def register():
    first_name = input("Enter your name: ") 
    last_name = input("Enter your surname: ") 
    username = input("Enter your username: ") 
    password = input("Enter your psasword: ") 
    user_register(first_name, last_name, username, password)

def login():
    username = input("Enter your username: ") 
    password = input("Enter your psasword: ") 
    user_login(username, password)








if __name__ == '__main__':
    main_menu()