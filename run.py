import random
import os
import colorama
from colorama import Fore, Back, Style
from words import easy_words_list, medium_words_list, hard_words_list
colorama.init(autoreset=True)

selected_word_difficulty = []

def print_main_logo():
    print()
    print("       ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗")
    print("       ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║")
    print("       ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║")
    print("       ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║")
    print("       ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║")
    print("       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print()


def start_menu():
    """
    Get input from the user.
    Run a while loop to collect valid data from the user via 
    the terminal, which must be 1 or 2. The loop will repeatedly 
    request data until it is valid.
    """
    print_main_logo()
    print('                         +--------------------------+')
    print('                         |    *** START MENU ***    |')
    print('                         +--------------------------+')
    print('                         |                          |')
    print('                         |       Play Game: 1       |')
    print('                         |                          |')
    print('                         |       Game Rules: 2      |')
    print('                         |                          |')
    print('                         |       Exit Game: 3       |')
    print('                         |                          |')
    print('                         +--------------------------+\n')

    while True:
        selected_menu_option = input("                         Please select an option: ")
        if selected_menu_option == '1':
            os.system('clear')
            difficulty_selection()
            return False
        elif selected_menu_option == '2':  
            os.system('clear')
            display_game_rules()
            return False
        elif selected_menu_option == '3':  
            exit()
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
        if int_user_input > 3:
            print(
                f"             {Fore.RED}Please enter a number provided, '{user_input}' is not an option.\n"
            )
    except ValueError:
        print(f"           {Fore.RED}Invalid selection, please try again by choosing a number.\n")
        return False
    
    return True

def difficulty_selection():
    global selected_word_difficulty
    print_main_logo()
    print('                        +---------------------------+')
    print('                        |  *** DIFFICULTY MENU ***  |')
    print('                        +---------------------------+')
    print('                        |                           |')
    print('                        |           Easy: 1         |')
    print('                        |                           |')
    print('                        |          Medium: 2        |')
    print('                        |                           |')
    print('                        |           Hard: 3         |')
    print('                        |                           |')
    print('                        |        Start Menu: 4      |')
    print('                        |                           |')
    print('                        +---------------------------+\n')

    while True:
        selected_difficulty_option = input("                        Please select an option: ")
        if selected_difficulty_option == '1':
            os.system('clear')
            selected_word_difficulty = easy_words_list
            return False
        elif selected_difficulty_option == '2':
            os.system('clear')
            selected_word_difficulty = medium_words_list
            return False
        elif selected_difficulty_option == '3':
            os.system('clear')
            selected_word_difficulty = hard_words_list
            return False
        elif selected_difficulty_option == '4':
            os.system('clear')
            start_menu()
            return False
        else:
            print()
            validate_menu_selection(selected_difficulty_option)


def display_game_rules():
    print('            +----------------------------------------------------+')
    print('            |                 *** RULES MENU ***                 |')
    print('            +----------------------------------------------------+')
    print('            |                                                    |')
    print('            |  - You will have 6 tries to guess a hidden word.   |')
    print('            |                                                    |')
    print('            |  - The higher the difficulty, the longer the word. |')
    print('            |                                                    |')
    print('            |  - You may guess single letters or you can try to  |')
    print('            |    guess the full word.                            |')
    print('            |                                                    |')
    print('            |  - Each will be counted as a guess!                |')
    print('            |                                                    |')
    print('            |  - Upon each correct guess, the hidden word will   |')
    print('            |    start to appear.                                |')
    print('            |                                                    |')
    print('            |  - Guess all of the letters or guess the word,     |')
    print('            |    and you will win the game.                      |')
    print('            |                                                    |')
    print('            |  - Run out of attempts, and the man will hang!     |')
    print('            |                                                    |')
    print('            |  - Best of luck, and watch your neck!              |')
    print('            |                                                    |')
    print('            +----------------------------------------------------+\n')

    while True:
        selected_rules_menu_option = input("                    Press Enter to return to Start Menu...")
        if selected_rules_menu_option == '':
            os.system('clear')
            start_menu()
            return False
        else:
            print()
            print(f"          {Fore.RED}Invalid input!")

def select_word(chosen_list):
    selected_word = random.choice(chosen_list)
    return selected_word.upper()


def display_game_info(hidden_word, letters_guessed, words_guessed, attempt_count):
    print("       +-------------------------------------------------------------+")
    print(display_hangman(attempt_count))
    print()
    print(f"                                {hidden_word}")
    print()
    print(f"                       Guessed letters: {', '.join(letters_guessed)}")
    print()
    print(f"                       Guessed words: {', '.join(words_guessed)}")
    print()


def play_game(word):
    hidden_word = " ".join("_" * len(word))
    guessed = False
    letters_guessed = set()
    words_guessed = set()
    attempt_count = 6

    display_game_info(hidden_word, letters_guessed, words_guessed, attempt_count)

    while not guessed and attempt_count > 0:
        user_guess = input("                       Please guess a letter or word: ").upper()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in letters_guessed:
                os.system('clear')
                print("       +-------------------------------------------------------------+")
                print(f"                 {Fore.RED}You have already guessed {user_guess}. Please try again!")
            elif user_guess not in word:
                os.system('clear')
                print("       +-------------------------------------------------------------+")
                print(f"                 {Fore.RED}'{user_guess}' is not in this word. Please try again!")
                attempt_count -= 1
                letters_guessed.add(user_guess)
            else:
                os.system('clear')
                print("       +-------------------------------------------------------------+")
                print(f"                        {Fore.GREEN}Well done! {user_guess} is in the word!")
                letters_guessed.add(user_guess)
                
                # Replacing letters in the hidden word
                hidden_word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    hidden_word_as_list[index * 2] = user_guess
                hidden_word = "".join(hidden_word_as_list)
                if "_" not in hidden_word:
                    guessed = True

        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in words_guessed:
                os.system('clear')
                print("       +-------------------------------------------------------------+")
                print(f"                 {Fore.RED}You have already guessed {user_guess}. Please try again!")
            elif user_guess != word:
                os.system('clear')
                print("       +-------------------------------------------------------------+")
                print(f"                      {Fore.RED}{user_guess} is not the correct word!")
                attempt_count -= 1
                words_guessed.add(user_guess)
            else:
                guessed = True
                hidden_word = word
        else:
            os.system('clear')
            print("       +-------------------------------------------------------------+")
            print(f"                      {Fore.RED}Invalid guess. Please try again!")
        display_game_info(hidden_word, letters_guessed, words_guessed, attempt_count)
    if guessed:
        os.system('clear')
        display_game_over()
        print(' ')
        display_win()
        print()
        print(f"      Congratulations, you guessed the correct word! The word was {word}.")
    else:
        os.system('clear')
        display_game_over()
        print(' ')
        display_lose()
        print()
        print(f"      {Fore.RED}You ran out of attempts. The word was {word}. Try again next time!")

def display_hangman(attempt_count):
    hangman_stage = ['''
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |    / \\
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |    /
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|
                                  |
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |     O
                                  |     |
                                  |
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |     O
                                  |
                                  |
                                  |
                                =========''', '''
                                  +-----+
                                  |     |
                                  |   
                                  |
                                  |
                                  |
                                =========''']

    return hangman_stage[attempt_count]

def end_game():
    while True:
        word = select_word(selected_word_difficulty)
        print()
        end_game_input = input("                             Play Again? (Y/N): ").upper()
        if end_game_input == "Y":
            os.system('clear')
            play_game(word)
        elif end_game_input == "N":
            os.system('clear')
            start_menu()
            play_game(word)
        else:
            print()
            print('                        Please select a valid option!')

def display_game_over():
    print()
    print('  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗')
    print('  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗')
    print('  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝')
    print('  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗')
    print('  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║')
    print('   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝')

def display_lose():
    print('       ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗')
    print('       ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝')
    print('        ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗')
    print('         ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝')
    print('          ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗ ')
    print('          ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝')

def display_win():
    print("            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗")
    print("            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║")
    print("             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║")
    print("              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║")
    print("               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║")
    print("               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝")

def main():
    global selected_word_difficulty
    start_menu()
    word = select_word(selected_word_difficulty)
    play_game(word)
    end_game()

main()


