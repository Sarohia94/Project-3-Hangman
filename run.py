# All code or resources used are credited in the README file.
import os
import random
from words import word_list
from hangman import HANGMAN


def get_random_word():
    """
    Gets a random word from words_list array from the word.py file.
    """
    word = random.choice(word_list)
    return word.upper()


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
            print("You've been hanged!")
            print(f"\nThe word was {word}")
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
    incorrect_letters = ""
    correct_letters = ""
    word = get_random_word()
    display_game(incorrect_letters, correct_letters, word)


main()
