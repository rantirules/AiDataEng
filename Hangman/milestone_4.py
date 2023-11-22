import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) #  int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = 5 # int - The number of lives the player has at the start of the game.
        self.word_list = [] # list - A list of words
        self.list_of_guesses = []  #  list - A list of the guesses that have already been tried. Set this to an empty list initially
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for w in self.word:
                if w == guess:
                    word_guessed[word_guessed.index(guess)] = guess
            num_letters -= 1
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in word.")
            print(f"You have {num_lives} left.")
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game = Hangman(['mangoes', 'banana'])
game.ask_for_input()