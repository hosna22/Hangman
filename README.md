# Hangman
A classic word-guessing game created using Python. This project is part of Data Analytics course with AiCore, demostarting how basic programming skills can be used to create an interactive and engaging application. Hangman is a timeless game where one player thinks of a word, and the other tries to guess it within a limited number of attempts.

## Getting started
I structured the game using a Hangman class to keep all attributes and methods in one place, keeping the code organised and easier to manage. The logic behind the game was divided into 2 methods: check_guess to check the player's guess against the secret word and ask_for_input to validate that the player has entered a single letter. For the overall flow of the game, I used a play_game function that creates an instance of the Hangman class and interacts with its methods. 

### Built with 
- Python version 3

### Prerequisites
- import random 

### Features 
#### Random Word Selection
- The game selects a random word from a predefined list for each round using the choice method from Python's random module.
<img width="383" alt="Screenshot 2025-01-08 at 14 32 34" src="https://github.com/user-attachments/assets/21b624c3-5952-474d-b07b-aeaf7c4c19cd" />


#### Word Progress Display
Players can see their progress with the word through placeholders for unrevealed letters. When a letter is guessed correctly, the letter is revealed in it's respective position.

#### Input Validation 
Player input is validated to allow only single alphabetical characters and prevent repeated guesses by informing players if they’ve already tried a letter.

#### Instant feedback 
The game provides instant feedback. Correct guesses reveal the corresponding letters in the word and incorrect guesses notify the player and display the remaining lives. 

### Installation instructions

## Usage instructions

## File structure of the project
