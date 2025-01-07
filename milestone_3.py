import random

word_list = ["Mango", "Blueberries", "Watermelon", "Kiwi", "Apples"]

secret_word = random.choice(word_list)
#print(secret_word)

def check_guess(guess):
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True: 
        guess = input("Enter a single letter: ").lower()
        #print(guess)
        if len(guess) == 1 and guess.isalpha() == True:
            break 
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()

    