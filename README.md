# Hangman Game

This is a simple Hangman game where the player tries to guess a word by entering characters one at a time. The player has a limited number of guesses before the game ends.

## How to Play
1. Run the game by executing the script.
2. You will be prompted to enter the name of the file containing words. Press Enter to use the default file `short_words.txt` or specify a custom file name.
3. The game will randomly select a word from the file and provide you with a hint by showing one of the characters.
4. Guess the word by entering characters one at a time. You have a total of 5 guesses.
5. If you correctly guess a character, it will be revealed in the word.
6. If you make an incorrect guess, part of the hangman figure will be drawn.
7. Keep guessing until you correctly guess the word or run out of guesses.

## Functions

- `read_file(file_name)`: Reads the content of a file line by line.
- `get_user_input()`: Prompts the user to input a character for guessing.
- `ask_file_name()`: Asks the user to input the name of the file containing words.
- `select_random_word(words)`: Randomly selects a word from a list of words.
- `random_fill_word(word)`: Randomly selects a character in the word to reveal.
- `is_missing_char(original_word, answer_word, char)`: Checks if a character is missing in the original word but present in the answer word.
- `fill_in_char(original_word, answer_word, char)`: Fills in the guessed character in the answer word.
- `do_correct_answer(original_word, answer, guess)`: Handles correct user guess.
- `do_wrong_answer(answer, number_guesses)`: Handles wrong user guess.
- `draw_figure(number_guesses)`: Draws the hangman figure based on the remaining number of guesses.
- `run_game_loop(word, answer)`: Runs the game loop for guessing the word.

## Usage
```bash
python hangman_game.py


## Note
    Make sure to have a file containing words to play the game. The default file short_words.txt is provided.