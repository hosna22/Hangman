import random

word_list = ["Mango", "Blueberries", "Watermelon", "Kiwi", "Apples"]

random_word = random.choice(word_list)

print(random_word)

guess = input("Enter a single letter: ")

def check_input():
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
    else: 
        print("Oops! That is not a valid input.")

check_input()
