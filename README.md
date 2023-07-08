# Hangman
Having a neck is something that most people will have in common. Personally, I like my neck intact. Welcome to the exciting game of Hangman! In this game, your linguistic skills will be put to the ultimate test. Hangman is a challenging experience that combines the thrill of word puzzles with the suspense of saving a life. 

The objective is simple yet thrilling: guess the hidden word by suggesting letters one at a time. But be warned, for every incorrect guess, another piece of the hangman will be assembled. With a limited number of attempts, your mental agility and vocabulary prowess will determine whether the innocent stick figure survives or meets an unfortunate demise. Can you unravel the word and emerge as the hero of this gripping tale? The stage is set, so let the guessing begin!

The live project can be accessed [here](https://hangman-md-95d75375f313.herokuapp.com/)

![Screenshot](documentation/start-menu-screen.png)

## UI/UX

### Design Overview
The game was ultimately designed to be interesting to look at as well as intuitive. All of the menus are clearly laid out with enough information to help a first time user to navigate through them with ease. The game provides input validation to assist the user in entering the correct data for the program to function correctly and is also designed to run continuously until the user decides to exit.

### Colour Scheme
[Colorama](https://pypi.org/project/colorama/) was used to apply colour to the text in the terminal. Colours were used to make the program more visually appealing more to give innate meanings to particular sections of the code.

**Colours Used**
- Inputs are displayed in white, this is due to white having the least confict and is easy to read.
- Menu borders are displayed in Cyan.
- Menu headings are displayed in Yellow.
- Errors are displayed in Red.
- Difficulty settings are displayed in Green, Yellow and Red ranging from easy to hard.
- Green and Red are used for win and loss case text.
- The revealed hidden word is displayed in Yellow at the end of the game.

## User Stories

1. As a new site user, I'd like to understand the site's goal so that I can determine whether I would like to use it or not.
2. As a new site user, I'd like to understand how to play the game.
3. As a new site user, I'd like the navigation to be simple and easy to understand.
4. As a new site user, I'd like to easily understand what input is needed on each step.
5. As a new site user, I'd like the game to test my knowledge and give me feedback on my progress.

## Flowchart

During the planning stages of this project, [Smartdraw](https://cloud.smartdraw.com/) was used to design the below flochart in order to plan the logic of program.

Throughout the development of the project, some new functions and display cases have been added; however, the base game functionality/logic has stayed quite similar to the initial idea.

![Screenshot](documentation/hangman-flowchart.png)

## Features

### Main Logo

- The main game logo is displayed on the start menu and difficulty selection menus. The logo was created with a [Text to ASCII Art](https://patorjk.com/software/taag/) generator. The logo itself is meaningful and intersting to look at. It further demonstrates what the program is about.

    ![Screenshot](documentation/main-logo.png)

### Start Menu

- The start menu consists of 3 separate options, and, prompts the user to enter information. Each option has a corresponding number. These numbers are what the user needs to enter to access these features in the program. In the event that the user enters invalid information, an error message will appear prompting them for the correct information.

    ![Screenshot](documentation/start-menu.png)