import random

def read_file(file_name):
    """
    Reads the content of a file line by line.
    
    Args:
        file_name (str): The name of the file to be read.
        
    Returns:
        list: A list containing each line of the file as a string.
    """
    file = open(file_name,'r')
    return file.readlines()

def get_user_input():
    """
    Prompts the user to input a character for guessing.
    
    Returns:
        str: The character entered by the user.
    """
    return input('Guess the missing letter: ')

def ask_file_name():
    """
    Asks the user to input the name of the file containing words.
    
    Returns:
        str: The name of the file to be used.
    """
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name

def select_random_word(words):
    """
    Randomly selects a word from a list of words.
    
    Args:
        words (list): A list of words from which to select.
        
    Returns:
        str: The randomly selected word.
    """
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word

def random_fill_word(word):
    """
    Randomly selects a character in the word to reveal.
    
    Args:
        word (str): The word to be filled.
        
    Returns:
        str: The word with a random character revealed.
    """
    index = random.randint(0, len(word)-1)
    display = ["_" for letter in word]
    display[index] = word[index]
    return ''.join(display)

def is_missing_char(original_word, answer_word, char):
    """
    Checks if a character is missing in the original word but present in the answer word.
    
    Args:
        original_word (str): The original word.
        answer_word (str): The word with guessed characters.
        char (str): The character to check.
        
    Returns:
        bool: True if the character is missing in the original word but present in the answer word, False otherwise.
    """
    if char in original_word and char not in answer_word:
        return True
    return False



def fill_in_char(original_word, answer_word, char):
    """
    Fills in the guessed character in the answer word.
    
    Args:
        original_word (str): The original word to be guessed.
        answer_word (str): The word with partially guessed characters.
        char (str): The character to be filled in.
        
    Returns:
        str: The updated answer word with the guessed character filled in.
    """
    answer_word = list(answer_word)
    for each_letter in range(0, len(original_word)):
        if char == original_word[each_letter] and answer_word[each_letter].find("_") != -1:
            answer_word[each_letter] = original_word[each_letter]
    return "".join(answer_word)


def do_correct_answer(original_word, answer, guess):
    """
    Handles correct user guess.
    
    Args:
        original_word (str): The original word to be guessed.
        answer (str): The current state of the word with guessed characters filled in.
        guess (str): The guessed character.
        
    Returns:
        str: The updated answer word after filling in the correct guess.
    """
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


def do_wrong_answer(answer, number_guesses):
    """
    Handles wrong user guess.
    
    Args:
        answer (str): The current state of the word with guessed characters filled in.
        number_guesses (int): The remaining number of guesses.
    """
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    if number_guesses == 0:
        print("""
  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
""")

        print('Sorry, you are out of guesses. The word was: '+answer)


def draw_figure(number_guesses):
    """
    Draws the hangman figure based on the remaining number of guesses.
    
    Args:
        number_guesses (int): The remaining number of guesses.
    """
    if number_guesses == 4:
        print("""/----
|
|
|
|
_______""")
              
    elif number_guesses == 3:
        print("""/----
|   0
|
|
|
_______""")
    elif number_guesses == 2:
        print("""/----
|   0
|   | 
|   | 
|   | 
_______""")
    elif number_guesses == 1 :
        print("""/----
|    0
|  /|\\
|   |
|   |  
_______""")
              
    else:
        print("""/----
|   0
|  /|\\
|   |
|  / \\
_______""")

def run_game_loop(word, answer):
    """
    Runs the game loop for guessing the word.
    
    Args:
        word (str): The word to be guessed.
        answer (str): The current state of the word with guessed characters filled in.
    """
    print("Guess the word: " + answer)
    number_guesses = 5
    correct_guesses = 0
    while number_guesses > 0:
        guess = get_user_input()
        if guess == 'exit' or guess == 'quit':
            print('Bye!')
            break

        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            if answer == word:  # Check if all letters are guessed correctly
                print_you_win()
                break
        else:
            number_guesses -= 1
            do_wrong_answer(word, number_guesses)

def print_you_win():
    win = "\u2713"  # U+2713
    text_length = len("YOU WIN!")
    font_size = 72
    for i in range(0, text_length):
        print(win, end="", flush=True)
    print("\r")
    print(win, end="", flush=True)
    print("\r")




if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

