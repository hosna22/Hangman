import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives  #number of lives the player has at the start of the game
        self.word = random.choice(word_list)  #word to be guessed
        self.word_guessed = ['_' for letter in self.word] #list of the letters of the word
        self.num_letters = len(self.word)  #number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = []  #A list of the guesses that have already been tried
    
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True: 
            guess = input("Enter a single letter: ").lower()
            #print(guess)
            if len(guess) != 1 and guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.") 
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)

                self.list_of_guesses = self.list_of_guesses.append(guess)

test = Hangman(["Mango", "Blueberries", "Watermelon", "Kiwi", "Apples"])
test.ask_for_input()
            
    