from milestone_2 import word


def check_guess(guess):
    guess.lower()
    #while True:
        # guess = input("Guess a letter: ")
        # if len(guess) == 1 and guess.isalpha():
        #     break
        # print("Invalid letter. Please, enter a single alphabetical character.")
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()