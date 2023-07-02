import random
import os
from words import word_list


print(' _')
print('| |')
print('| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __')
print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print('| | | | (_| | | | | (_| | | | | | | (_| | | | |')
print('|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|')
print('                    __/ |')
print('                   |___/')


def start_menu():
    """
    Get input from the user.
    Run a while loop to collect valid data from the user via 
    the terminal, which must be 1 or 2. The loop will repeatedly 
    request data until it is valid.
    """
    print('          +--------------------------+')
    print('          |                          |')
    print('          |       Play Game: 1       |')
    print('          |                          |')
    print('          |       Game Rules: 2      |')
    print('          |                          |')
    print('          +--------------------------+\n')

    while True:
        selected_menu_option = input("          Please select an option: ")
        if selected_menu_option == '1':
            os.system('clear')
            difficulty_selection()
            print('start game selected')
            return False
        elif selected_menu_option == '2':
            # show_game_rules()
            os.system('clear')
            print('game rules selected')
            return False
        else:
            print()
            validate_menu_selection(selected_menu_option)


def validate_menu_selection(user_input):
    """
    Inside the try, converts start_menu input to an integer.
    Raises ValueError if the value is greater than 2 or if
    the string cannot be converted into an int.
    """
    try:
        int_user_input = int(user_input)
        if int_user_input > 2:
            raise ValueError(
                f"Please enter a number provided, '{user_input}' is not an option."
            )
    except ValueError as e:
        print(f"Invalid selection: {e}, please try again.\n")
        return False
    
    return True


start_menu()

