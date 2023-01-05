import random
from words import word_list

import os


def get_random_word():
    """
    Gets a random word from words_list array from the word.py file.
    """
    word = random.choice(word_list)
    return word.upper()


def display_game(incorrect_letters, correct_letters, word):
    """
    Displays hangman game to the user and what letters the user has guessed
    """
    lives = 6
    print(f"You have {len(HANGMAN)-1} lives!")

    print(f"\nThere are {len(word)} letters in this word")

    print(word)  # check

    guess_word = "_" * len(word)

    game_over = False
    while not game_over and lives > 0:
        print(HANGMAN[len(incorrect_letters)])
        print(f"\nWord: {guess_word}\n")
        guess = input("\nPlease guess a letter:").upper()

        try:
            if len(guess) == 1 and guess.isalpha():
                if guess not in word:
                    os.system("clear")
                    print(guess, "is not in the word\n")
                    incorrect_letters = incorrect_letters + guess
                    lives -= 1
                    print(f"You have {lives} lives remaining!")
                    print('\nIncorrect guesses:', end=" ")
                    for guess in incorrect_letters:
                        print(guess, end=" ")

                else:
                    os.system("clear")
                    print("\nYes!", guess, "is in the word!")
                    correct_letters = correct_letters + guess
                
                    word_as_list = list(guess_word)
                    indices = [i for i, letter in enumerate(word)
                               if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                        guess_word = "".join(word_as_list)
            else:
                os.system("clear")
                raise ValueError()
        except ValueError as e:
            print(f"\nInvalid data: {e} please enter a single letter")


HANGMAN = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


def main():
    incorrect_letters = ""
    correct_letters = ""
    word = get_random_word()
    display_game(incorrect_letters, correct_letters, word)


main()