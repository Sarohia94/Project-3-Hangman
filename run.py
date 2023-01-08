# All code or resources used are credited in the README file.
import os
import random
from words import word_list
from hangman import HANGMAN

NAME = ""


def get_random_word():
    """
    Gets a random word from words_list array from the word.py file.
    """
    word = random.choice(word_list)
    return word.upper()


def start_game():
    """
    Welcomes user and introduces game
    """
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    \n""")
    print("Let's play hangman!\n")


def player_name():
    """
    Requests users name.
    This will be used when user is either hanged or guesses the full word.
    """
    global NAME
    while True:
        NAME = input("What is your name?\n").upper()
        if NAME.isalpha():
            break
        os.system("clear")
        start_game()
        print("Please enter a valid name using letters.")
    os.system("clear")
    print(f"Welcome {NAME}!")
    return NAME


def menu():
    """
    Requests user to choose from menu.
    Option to play game or learn how to play.
    """
    print(f"""{NAME} would you like to:\n
          1. Start game\n
          2. Learn how to play?\n""")
    print("Please enter 1 to start game or 2 to learn how to play.\n")
    choice_made = False
    while choice_made is False:
        menu_choice = input("Number: ")
        try:
            if menu_choice == "1":
                return menu_choice
                choice_made = True
            if menu_choice == "2":
                return menu_choice
                choice_made = True
            else:
                os.system("clear")
                start_game()
                raise ValueError("Please enter 1 to start game" +
                                 " or 2 to learn how to play.\n")
        except ValueError as e:
            print(f"\nInvalid data:\n{e}")


def how_to_play():
    """
    Instructions for user unfamiliar to the game on how to play.
    """
    os.system("clear")
    print("""
      Hangman is a word guessing game.\n
      The object of the game is to figure out the unknown word by guessing
      letters.\n
      The length of the word will be provided and it will be marked by
      underscores for each letter.\n
      You will be prompted to guess a single letter from the alphabet.\n
      If the letter is in the unknown word it will display by replacing the
      underscores.\n
      If the guessed letter is not in the unknown word you will lose a try.\n
      This will correspond to a person on the gallow being drawn,
      one part for each incorrect letter guessed.\n
      As such you will have 6 tries to guess before you are hanged and
      lose the game!\n
      i.e. in the order: head, body, left arm, right arm, left leg, right leg.
      """)
    print(f"Good luck {NAME}! Guess the word and win the game!\n")
    print("Please enter 1 to start game or 2 to return to menu.\n")
    choice_made = False
    while choice_made is False:
        menu_choice = input("Number: ")
        try:
            if menu_choice == "1":
                start_game()
                choice_made = True
            if menu_choice == "2":
                menu()
                choice_made = True
            else:
                os.system("clear")
                start_game()
                raise ValueError("Please enter 1 to start game" +
                                 " or 2 to return to menu.\n""")
        except ValueError as e:
            print(f"\nInvalid data: {e}")


def display_game(incorrect_letters, correct_letters, word):
    """
    Displays hangman game to the user.
    If user runs out of tries without completing the word they're hanged.
    If the user completes the word without running out of tries they win.
    """
    tries = 6
    guess_word = "_" * len(word)
    word = get_random_word()

    print(f"You have {len(HANGMAN)-1} attempts to guess the word!")

    print(f"\nThere are {len(word)} letters in this word")

    print(word)  # check

    game_over = False
    while not game_over and tries > 0:
        print(HANGMAN[len(incorrect_letters)])
        print(f"\nWord: {guess_word}\n")
        guess = input("\nPlease guess a letter:").upper()
        if tries == 0:
            game_over = True
            print("You've been hanged!\n")
            print(f"The word was {word}\n")
        else:
            if len(word) == len(correct_letters):
                game_over = True
                print("Congratulations! You've guessed the word.")


# Code below was originally in display_game but became too complex
# This is to be organised in to smaller functions

# try:
#    if len(guess) == 1 and guess.isalpha():
#        if guess not in word:
#            os.system("clear")
#            print(guess, "is not in the word\n")
#            incorrect_letters = incorrect_letters + guess
#            tries -= 1
#            print(f"You have {tries} attempts remaining!")
#            print('\nIncorrect guesses:', end=" ")
#            for guess in incorrect_letters:
#                print(guess, end=" ")

#        else:
#            os.system("clear")
#            print("\nYes!", guess, "is in the word!")
#            correct_letters = correct_letters + guess
#            print(correct_letters)
#            word_as_list = list(guess_word)
#            indices = [i for i, letter in enumerate(word)
#                       if letter == guess]
#            for index in indices:
#                word_as_list[index] = guess
#                guess_word = "".join(word_as_list)

#    else:
#        os.system("clear")
#        if len(guess) > 1:
#            raise ValueError(f"You have guessed {len(guess)} "
#                             + "characters. Please guess 1 letter")
#        if not guess.isalpha():
#            raise ValueError("Please guess a letter.")

# except ValueError as e:
#    print(f"\nInvalid data: {e}")


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

    incorrect_letters = ""
    correct_letters = ""
    word = get_random_word()
    display_game(incorrect_letters, correct_letters, word)


main()
