def print_menu(options):
    for id,option in enumerate(options,1):
        print(f"{id}. {option}")

def user_choice(max_choice):
    choice = int(input("Enter the choice: "))
    try:
        if 1 <= choice <= max_choice :
            return choice
        else:
            print(f"Enter number between 1 and {max_choice}!")
    except:
        print("Pls Enter valid number!!!")