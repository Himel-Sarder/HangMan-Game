import random

# List of words for the game
words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pineapple', 'strawberry', 'watermelon',
         'peach', 'pear', 'plum', 'mango', 'lemon', 'lime', 'blueberry', 'raspberry',
         'apricot', 'blackberry', 'cherry', 'coconut', 'cranberry', 'fig', 'guava',
         'nectarine', 'papaya', 'passionfruit', 'pomegranate', 'melon', 'dragonfruit']

# ASCII art for the hangman stages
hangman_stages = [
    '''
    +---+
        |
        |
        |
        |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
        |
        |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  ========''',
  '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========'''
]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the hangman
def display_hangman(stage):
    print(hangman_stages[stage])

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

# Run the game
print("""
Welcome to Hangman!
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |                      
                      |___/    
Coded by - 
Himel Sarder
Dept. of Computer Science and Engineering, BSFMSTU
""")

play_again = 'yes'
while play_again == 'yes':
    print()
    print("=" * 50)
    print()
    word = choose_word()
    guessed_letters = []
    attempts = 6
    stage = 0

    while attempts > 0:
        print("\nAttempts left:", attempts)
        display_hangman(stage)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            stage += 1
            print("Incorrect guess!")
            if attempts == 0:
                display_hangman(stage)
                print("You lose! The word was:", word)
                break
        else:
            if '_' not in display_word(word, guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Thanks for playing!")
