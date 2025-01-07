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
            for index, letter in enumerate(self.word.lower()):
                if letter.lower() == guess:
                    self.word_guessed[index] = f"{letter}"
            print (self.word_guessed)

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives = self.num_lives - 1
            print(f"you have {self.num_lives} lives left")

    def ask_for_input(self):
        print(self.word_guessed)
        while True: 
            guess = input("Enter a single letter: ").lower()

            if len(guess) > 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.") 
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

test = Hangman(["Blueberries", "Papaya", "Kiwi", "Apples", "Banana"])
test.ask_for_input()
            
    