import random

class Hangman:
    """
    Attributes:
        word_list (list): list of words for player to guess
        num_lives (int): number of lives the player has at the start of the game
        word (str): word to be guessed
        word_guessed (list): list of empty spaces for the letters of the word
        num_letter (int): number of unique letters in the word that have not been guessed yet
        list_of_guesses (list): list of the guesses that have already been tried
        """
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives 
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word] 
        self.num_letters = len(self.word)  
        self.list_of_guesses = [] 
    
    def check_guess(self,guess):
        """
        This method checks if the the user input guess is in the word to be guessed. 
        
        The method passes the guess from the user as a parameter. It checks if the guess 
        is in the random word to be guessed and returns the letters position in the word 
        if guessed correctly. If guessed incorrectly, it reduces the players lives by 1. 
        """
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
        """
        This method checks if the the user input is a single letter and acceptable input. 
        
        The method asks the player to input their guess and checks if it is one character 
        and alphabetical. If the input is not correct, the error is stated and the user is 
        asked to input again. If the input passes the checks, it is appended to a list which 
        stores the players guesses to avoid the same letter being guessed twice.
        """
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
            
    