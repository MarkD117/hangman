import random
import os
import colorama
from colorama import Fore, Back, Style
from words import easy_words_list, medium_words_list, hard_words_list
colorama.init(autoreset=True)

# Initialising an empty list for difficulty selected by user.
selected_word_difficulty = []


def print_main_logo():
    """
    Prints the main logo of the game.
    """
    print()
    print(f"       ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗")
    print(f"       ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║")
    print(f"       ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║")
    print(f"       ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║")
    print(f"       ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║")
    print(f"       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print()


def start_menu():
    """
    Displays start menu.
    Get input from the user.
    Run a while loop to collect valid data from the user via
    the terminal, which must be 1, 2 or 3. The loop will repeatedly
    request data until it is valid.
    """
    print_main_logo()
    print(f"                         {Fore.CYAN}+--------------------------+")
    print(f"                         {Fore.CYAN}|    {Fore.YELLOW}*** START MENU ***    {Fore.CYAN}|")
    print(f"                         {Fore.CYAN}+--------------------------+")
    print(f"                         {Fore.CYAN}|                          |")
    print(f"                         {Fore.CYAN}|       {Fore.RESET}Play Game: 1       {Fore.CYAN}|")
    print(f"                         {Fore.CYAN}|                          |")
    print(f"                         {Fore.CYAN}|       {Fore.RESET}Game Rules: 2      {Fore.CYAN}|")
    print(f"                         {Fore.CYAN}|                          |")
    print(f"                         {Fore.CYAN}|       {Fore.RESET}Exit Game: 3       {Fore.CYAN}|")
    print(f"                         {Fore.CYAN}|                          |")
    print(f"                         {Fore.CYAN}+--------------------------+\n")

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
            print()
            print(f"                            {Fore.RED}Game has been exited!")
            exit()
            return False
        else:
            print()
            validate_menu_selection(selected_menu_option)


def validate_menu_selection(user_input):
    """
    Inside the try, converts start_menu input to an integer.
    Raises ValueError if the value is greater than 3 or if
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
    """
    Displays difficulty menu
    Get input from the user, similar to start_game function.
    Run a while loop to collect valid data from the user via
    the terminal, which must be between 1 - 4. The loop will repeatedly
    request data until it is valid. Each difficulty will set value of
    selected_word_difficulty list.
    """
    global selected_word_difficulty
    print_main_logo()
    print(f"                        {Fore.CYAN}+---------------------------+")
    print(f"                        {Fore.CYAN}|  {Fore.YELLOW}*** DIFFICULTY MENU ***  {Fore.CYAN}|")
    print(f"                        {Fore.CYAN}+---------------------------+")
    print(f"                        {Fore.CYAN}|                           |")
    print(f"                        {Fore.CYAN}|           {Fore.GREEN}{Style.BRIGHT}Easy: 1         {Fore.CYAN}{Style.NORMAL}|")
    print(f"                        {Fore.CYAN}|                           |")
    print(f"                        {Fore.CYAN}|          {Fore.YELLOW}{Style.BRIGHT}Medium: 2        {Fore.CYAN}{Style.NORMAL}|")
    print(f"                        {Fore.CYAN}|                           |")
    print(f"                        {Fore.CYAN}|           {Fore.RED}{Style.BRIGHT}Hard: 3         {Fore.CYAN}{Style.NORMAL}|")
    print(f"                        {Fore.CYAN}|                           |")
    print(f"                        {Fore.CYAN}|        {Fore.RESET}Start Menu: 4      {Fore.CYAN}|")
    print(f"                        {Fore.CYAN}|                           |")
    print(f"                        {Fore.CYAN}+---------------------------+\n")

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
    """
    Displays rules menu explaining to user how to play the game.
    Run a while loop to collect valid data from the user via
    the terminal. The loop will repeatedly request data until it is valid.
    """
    print(f"            {Fore.CYAN}+----------------------------------------------------+")
    print(f"            {Fore.CYAN}|                 {Fore.YELLOW}*** RULES MENU ***                 {Fore.CYAN}|")
    print(f"            {Fore.CYAN}+----------------------------------------------------+")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- You will have 6 tries to guess a hidden word.   {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- The higher the difficulty, the longer the word. {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- You may guess single letters or you can try to  {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|    {Fore.RESET}guess the full word.                            {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- Each will be counted as a guess!                {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- Upon each correct guess, the hidden word will   {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|    {Fore.RESET}start to appear.                                {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- Guess all of the letters or guess the word,     {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|    {Fore.RESET}and you will win the game.                      {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- Run out of attempts, and the man will hang!     {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}|  {Fore.RESET}- Best of luck, and watch your neck!              {Fore.CYAN}|")
    print(f"            {Fore.CYAN}|                                                    |")
    print(f"            {Fore.CYAN}+----------------------------------------------------+\n")

    while True:
        selected_rules_menu_option = input("                    Press Enter to return to Start Menu...")
        if selected_rules_menu_option == '':
            os.system('clear')
            start_menu()
            return False
        else:
            print()
            print(f"                                {Fore.RED}Invalid input!")
            print()


def select_word(chosen_list):
    """
    Selects a random word from chosen difficulty list.
    Returns word converted to uppercase.
    """
    selected_word = random.choice(chosen_list)
    return selected_word.upper()


def display_game_info(hidden_word, letters_guessed, words_guessed, attempt_count):
    """
    Displays constantly updating game information to the user,
    """
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
    """
    Handles main game functionality and logic. 'Word' parameter is the
    chosen word from the select_word funtion. Runs a while loop to check user inputs.
    Based on user input custom outputs are shown. While loop will continously ask for
    input until user runs out of tries or guesses correct word.
    """

    # Adds spaces between underscores to see word length easier
    hidden_word = " ".join("_" * len(word))
    guessed = False
    letters_guessed = set()
    words_guessed = set()
    attempt_count = 6

    display_game_info(hidden_word, letters_guessed, words_guessed, attempt_count)

    while not guessed and attempt_count > 0:
        user_guess = input("                       Please guess a letter or word: ").upper()
        # Handling single letter input
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

                # Replaces letters in the hidden word
                hidden_word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    # Index multiplied by 2 to account for additional spaces
                    hidden_word_as_list[index * 2] = user_guess
                hidden_word = "".join(hidden_word_as_list)

                # If no underscores left in the word, user has guessed correctly
                if "_" not in hidden_word:
                    guessed = True

        # Handling full word input
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

    # Output for WIN case
    if guessed:
        os.system('clear')
        display_game_over_win()
        print(' ')
        display_win()
        print()
        print(f"      {Fore.GREEN}Congratulations, the word was {Fore.YELLOW}{word}{Fore.GREEN}. You guessed correctly!.")
    
    # Output for LOSE case
    else:
        os.system('clear')
        display_game_over_lose()
        print(' ')
        display_lose()
        print()
        print(f"      {Fore.RED}You ran out of attempts. The word was {Fore.YELLOW}{word}{Fore.RED}. Try again next time!")


def display_hangman(attempt_count):
    """
    Holds stages for hangman. Stages are displayed based on attempt count.
    Initialised to 6, the 6th index will be shown. Each incorrect guess
    will decrement attempt count showing the next stage.
    """
    hangman_stage = ['''
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |    / \\
                                  |
                                =========''', f'''{Fore.RED}
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |    /
                                  |
                                =========''', f'''{Fore.YELLOW}
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|\\
                                  |
                                  |
                                =========''', f'''{Fore.YELLOW}
                                  +-----+
                                  |     |
                                  |     O
                                  |    /|
                                  |
                                  |
                                =========''', f'''{Fore.GREEN}
                                  +-----+
                                  |     |
                                  |     O
                                  |     |
                                  |
                                  |
                                =========''', f'''{Fore.GREEN}
                                  +-----+
                                  |     |
                                  |     O
                                  |
                                  |
                                  |
                                =========''', f'''{Fore.GREEN}
                                  +-----+
                                  |     |
                                  |
                                  |
                                  |
                                  |
                                =========''']

    return hangman_stage[attempt_count]


def end_game():
    """
    Runs after game is finished. While loop asks user for input.
    User can restart the game again or can go back to start menu.
    While loop will run until user enters valid input.
    """
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
            print(f"                        {Fore.RED}Please select a valid option!")


def display_game_over_lose():
    """
    Output for game over screen if user loses.
    """
    print()
    print(f"{Fore.RED}  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
    print(f"{Fore.RED}  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(f"{Fore.RED}  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(f"{Fore.RED}  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(f"{Fore.RED}  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(f"{Fore.RED}   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")


def display_lose():
    """
    Output for loss screen
    """
    print(f"{Fore.RED}       ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗")
    print(f"{Fore.RED}       ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝")
    print(f"{Fore.RED}        ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗")
    print(f"{Fore.RED}         ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝")
    print(f"{Fore.RED}          ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗ ")
    print(f"{Fore.RED}          ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝")


def display_game_over_win():
    """
    Output for game over screen if user wins.
    """
    print()
    print(f"{Fore.GREEN}  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
    print(f"{Fore.GREEN}  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(f"{Fore.GREEN}  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(f"{Fore.GREEN}  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(f"{Fore.GREEN}  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(f"{Fore.GREEN}   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")


def display_win():
    """
    Output for win screen
    """
    print(f"{Fore.GREEN}            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗")
    print(f"{Fore.GREEN}            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║")
    print(f"{Fore.GREEN}             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║")
    print(f"{Fore.GREEN}              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║")
    print(f"{Fore.GREEN}               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║")
    print(f"{Fore.GREEN}               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝")


def main():
    global selected_word_difficulty
    start_menu()
    word = select_word(selected_word_difficulty)
    play_game(word)
    end_game()


main()
