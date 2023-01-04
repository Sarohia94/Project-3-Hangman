import random
from words import word_list

print(word_list)  # check


def get_random_word():
    """
    Gets a random word from words_list array from the word.py file.
    """
    word = random.choice(word_list)
    return word.upper()


print(get_random_word())  # check


def display_game(incorrect_letters, correct_letters, word):
    """
    Displays hangman game to the user and what letters the user has guessed
    """
    print(HANGMAN[len(incorrect_letters)])

    print(f"There are {len(word)} letters in this word")

    guess_word = "_" * len(word)
    print(f"Word: {guess_word} \n")


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
    word = get_random_word()
    incorrect_letters = ""
    correct_letters = ""
    display_game(incorrect_letters, correct_letters, word)


main()