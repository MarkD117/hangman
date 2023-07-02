import random
from words import word_list


print(' _')
print('| |')
print('| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __')
print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print('| | | | (_| | | | | (_| | | | | | | (_| | | | |')
print('|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|')
print('                    __/ |')
print('                   |___/')
print('          +--------------------------+')
print('          |                          |')
print('          |       Play Game: 1       |')
print('          |                          |')
print('          |       Game Rules: 2      |')
print('          |                          |')
print('          +--------------------------+\n')

def start_menu():
    """
    Get input from the user.
    Run a while loop to collect valid data from the user via 
    the terminal, which must be 1 or 2. The loop will repeatedly 
    request data until it is valid.
    """
    while True:
        selected_menu_option = input("          Please select an option: ")
        if selected_menu_option == '1':
            # difficulty_selection()
            print('start game selected')
            return False
        elif selected_menu_option == '2':
            # show_game_rules()
            print('game rules selected')
            return False
        else:
            print()
            validate_menu_selection(selected_menu_option)

start_menu()

