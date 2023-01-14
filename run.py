# All code and resources used are credited in the README file.
import os
import random
from time import sleep
from termcolor import colored
from words import word_list
from hangman import HANGMAN, WELCOME, GAME_OVER, WIN, BYE

NAME = ""
TRIES = 6
INCORRECT = ""
CORRECT = ""
WORD = ""
GUESS_WORD = ""


def start_game():
    """
    Displays hangman name with message to play.
    """
    print(colored(WELCOME, "magenta"))
    print("Let's play hangman!\n")
    print(colored(HANGMAN[6], "yellow", attrs=["bold"]))


def player_name():
    """
    Requests users name.
    This is used througout the game to engage with the user directly.
    Error messages are raised for invalid input.
    """
    global NAME
    while True:
        NAME = input(colored("\nWhat is your name?\n", "cyan")).upper()
        if NAME.isalpha():
            break
        os.system("clear")
        start_game()
        print(colored("\nPlease enter a valid name using letters.", "red"))
    os.system("clear")
    print(colored(f"Welcome {NAME}!\n", "magenta"))
    return NAME


def menu():
    """
    Requests user to choose from menu.
    Option to play game or learn how to play.
    Error messages are raised for invalid input.
    """
    print(f"""{NAME}, would you like to:\n
          1. Play the game\n
          2. Learn how to play?\n""")
    print(colored("Please enter 1 to play the game or 2 to learn how to play.",
                  "cyan"))

    choice_made = False
    while choice_made is False:
        menu_choice = input("\nNumber: \n")
        try:
            if menu_choice == "1":
                choice_made = True
                return menu_choice
            elif menu_choice == "2":
                choice_made = True
                return menu_choice
            else:
                os.system("clear")
                start_game()
                raise ValueError("Please enter 1 to play game" +
                                 " or 2 to learn how to play.\n")
        except ValueError as e:
            print(colored(f"\nInvalid data:\n{e}", "red"))


def how_to_play():
    """
    Instructions for user on how to play the game.
    User is then requested to enter 1 to play the game.
    Error messages are raised for invalid input.
    """
    os.system("clear")
    print("""
      Hangman is a word guessing game.\n
      The object of the game is to figure out the unknown word by guessing
      letters.\n
      If the letter is in the unknown word it will display.\n
      If the guessed letter is not in the unknown word you will lose a try.\n
      This will correspond to a person on the gallow being drawn,
      one part for each incorrect letter guessed.\n
      i.e. in the order: head, body, left arm, right arm, left leg, right
      leg.\n
      As such you will have 6 tries to guess before you are hanged and
      lose the game!
      """)
    print(colored("Now you know the rules, please enter 1 to play game.\n",
                  "cyan"))

    choice_made = False
    while choice_made is False:
        menu_choice = input("Number: \n")
        try:
            if menu_choice == "1":
                display_game()
                choice_made = True
            else:
                os.system("clear")
                start_game()
                raise ValueError("Please enter 1 to play the game.\n")
        except ValueError as e:
            print(colored(f"\nInvalid data: {e}", "red"))


def get_random_word():
    """
    Gets a random word from words_list array from the word.py file.
    """
    global WORD
    WORD = random.choice(word_list)
    return WORD.upper()


def display_game():
    """
    Displays hangman game to the user.
    If user runs out of tries without completing the word they're hanged.
    If the user completes the word without running out of tries they win.
    """
    os.system("clear")
    global TRIES
    global GUESS_WORD
    global INCORRECT
    global CORRECT

    TRIES = 6
    INCORRECT = ""
    CORRECT = ""

    WORD = get_random_word()
    GUESS_WORD = "_" * len(WORD)
    print(colored(f"Good luck {NAME}! Guess the word and win the game!\n",
                  "magenta"))
    print("Hint: the word to guess relates to animals...\n")
    print(f"You have {len(HANGMAN)-1} attempts to guess the word.")
    print(f"\nThere are {len(WORD)} letters in this word.")

    game_over = False
    while not game_over and TRIES > 0:
        print(colored(HANGMAN[len(INCORRECT)], "yellow", attrs=["bold"]))
        print(f"\nWord: {GUESS_WORD}\n")
        ask_for_input()
        if len(HANGMAN)-1 == len(INCORRECT):
            game_over = True
            os.system("clear")
            print(colored(GAME_OVER, "green"))
            print("\nOh no! You've been hanged!\n")
            print(colored(HANGMAN[6], "red", attrs=["bold"]))
            print(f"\nThe word was {WORD}\n")
            play_again()
        else:
            if "_" not in GUESS_WORD:
                game_over = True
                os.system("clear")
                print(colored(WIN, "yellow"))
                print(f"Well done {NAME}!" +
                      f" The word was {WORD}, you guessed right!\n")
                play_again()


def ask_for_input():
    """
    While the user still has tries, user input to guess is requested.
    If guess is valid then aslong as it hasn't been already guessed,
    the check_correct function is called to check if it is in the word.
    Otherwise if guess is invalid error messages are raised.
    """
    check = True
    guess = ""
    while check:
        guess = input(colored("\nPlease guess a letter: \n", "cyan")).upper()
        try:
            if len(guess) == 1 and guess.isalpha():
                if guess in INCORRECT or guess in CORRECT:
                    os.system("clear")
                    raise ValueError("You've already guessed this letter",
                                     guess)
                else:
                    check_correct(guess)
            if len(guess) > 1:
                os.system("clear")
                raise ValueError(f"You have guessed {len(guess)} "
                                 + "characters. Please guess 1 letter.")
            if not guess.isalpha():
                os.system("clear")
                raise ValueError("Please guess a letter.")
        except ValueError as e:
            print(colored(f"\nInvalid data: {e}", "red"))
        check = False
        return guess


def check_correct(guess):
    """
    Checks if guess is in the word.
    If so, correct letters are updated and letter is printed to guess_word.
    If not then incorrect letters are updated and is printed to the screen,
    as a result, the user loses a try.
    """
    global INCORRECT
    global CORRECT
    global GUESS_WORD
    global TRIES

    if guess in WORD.upper():
        os.system("clear")
        print("\nYes!", guess, "is in the word!")
        CORRECT = CORRECT + guess
        word_as_list = list(GUESS_WORD)
        indices = [i for i, letter in enumerate(WORD.upper())
                   if letter == guess]
        for index in indices:
            word_as_list[index] = guess
            GUESS_WORD = "".join(word_as_list)
    else:
        os.system("clear")
        print(guess, "is not in the word.\n")
        INCORRECT = INCORRECT + guess
        TRIES -= 1
        print(f"You have {TRIES} attempts remaining!")
        print("\nIncorrect guesses: ", end=" ")
        if TRIES > 0:
            for guess in INCORRECT:
                print(guess, end=" ")


def play_again():
    """
    The user is given the option to play again.
    If the user chooses not to play a good bye message
    is displayed before returning user to start_game.
    """
    sleep(3)
    while True:
        if input(colored(F"{NAME} would you like to play again?" +
                         " Enter any key to quit or Y to play again: \n",
                         "cyan")).upper() == "Y":
            os.system("clear")
            display_game()
        else:
            os.system("clear")
            print(colored(BYE, "cyan"))
            print(colored(f"Thanks for playing {NAME}!", "magenta"))
            sleep(3)
            os.system("clear")
            main()


def main():
    """
    Run all program functions
    """
    start_game()
    player_name()
    menu_choice = menu()
    if menu_choice == "1":
        display_game()
    elif menu_choice == "2":
        how_to_play()
    else:
        return


main()
