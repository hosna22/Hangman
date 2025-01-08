# Hangman
A classic word-guessing game created using Python. This project is part of Data Analytics course with AiCore, demostarting how basic programming skills can be used to create an interactive and engaging application. Hangman is a timeless game where one player thinks of a word, and the other tries to guess it within a limited number of attempts.

This project taught me how to use classes to model real-world concepts, like a game, by defining attributes to manage the game's state and methods to control its behavior. I learned how to interact with class instances to handle the game's flow and use this in a function. Encapsulating the game's logic in a class made the code more modular so I could easily amend and adapt it.

## Getting started
I structured the game using a Hangman class to keep all attributes and methods in one place, keeping the code organised and easier to manage. The logic behind the game was divided into 2 methods: check_guess to check the player's guess against the secret word and ask_for_input to validate that the player has entered a single letter. For the overall flow of the game, I used a play_game function that creates an instance of the Hangman class and interacts with its methods. 

### Built with 
- Python version 3

### Prerequisites
- <img width="224" alt="Screenshot 2025-01-08 at 15 15 37" src="https://github.com/user-attachments/assets/9e116031-7a44-4338-b004-1f4fc039814e" />

### Features

#### Random Word Selection
- The game selects a random word from a predefined list for each round using the choice method from Python's random module.
<img width="383" alt="Screenshot 2025-01-08 at 14 32 34" src="https://github.com/user-attachments/assets/21b624c3-5952-474d-b07b-aeaf7c4c19cd" />


#### Word Progress Display
- Players can see their progress with the word through placeholders for unrevealed letters. When a letter is guessed correctly, the letter is revealed in it's respective position.
<img width="224" alt="Screenshot 2025-01-08 at 14 53 08" src="https://github.com/user-attachments/assets/f45ecbb4-5d5b-44c8-9c44-5c3b51716fe1" />

#### Input Validation 
Player input is validated to allow only single alphabetical characters and prevent repeated guesses by informing players if they’ve already tried a letter.

#### Instant feedback 
The game provides instant feedback. Correct guesses reveal the corresponding letters in the word and incorrect guesses notify the player and display the remaining lives. 

### Installation instructions (macOS)
1. Install homebrew
2. Install miniconda
<img width="348" alt="Screenshot 2025-01-08 at 15 05 07" src="https://github.com/user-attachments/assets/b51093e4-d005-4038-b60c-d8658ccfb7a7" />
3. Intall python
<img width="224" alt="Screenshot 2025-01-08 at 15 06 13" src="https://github.com/user-attachments/assets/5a60c054-d7d4-4129-ad18-b871e9feed84" />
4. Intall VS Code
<img width="356" alt="Screenshot 2025-01-08 at 15 07 17" src="https://github.com/user-attachments/assets/8afa6ae0-dbe6-4938-bc71-0bf248ad94f9" />


