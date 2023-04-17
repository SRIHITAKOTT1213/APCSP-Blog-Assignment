import random

# This is what is shown to the user each time they guess wrong (the image changes by adding one limb for each wrong answer)
Hangman = ['''
    +---+
    |   |
        |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
    =========''',  '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
    =========''']

# This is a list of words, and one of these words will be chosen at random for the user to guess
words_list = ["love", 'free', "subway", "school", "break", "pencil", "backpack", "airpods", "phone", "summer", "college", "balloon",
            "vacation", "december", "summer", "cake", "airplane", "chess", "flask", "torch", "fan", "blanket", "flower", "trophie", 
            "mentos", "piano", "water", "music", "computer", "headphones", "suitcase", "instrument", "bed", "people", "television",
            "party", "spring", "dancing", "bottle", "english", "spanish", "fun", "california", "time", "airport", "gym", "outside"]

# This makes it so the user has until the last picture in the "Hangman" list to guess the entire word (which is about 7 wrong guesses before the user loses the game)
max_wrong = len(Hangman)

# Initializing our variables

# picking a word randomly
word = random.choice(words_list)
# dashes for each letter that is in the word (in other words the length)
current_guess = "_" * len(word)

# The number of wrong guesses 
incorrect_guess = 0

# The number of used letters

used_letters = []

print("Welcome to Hangman! Try to Guess the Word")


while incorrect_guess < max_wrong and current_guess != word:
    print(Hangman[incorrect_guess])

    print("You have used the following letters: ", used_letters)

    print("So far, the word is: ", current_guess)

    guess = input("Enter your Guess:")

    guess = guess.lower()

# This is to check to see if the letter was already used
    while guess in used_letters:
        print("You already used this letter")
        guess = input("Enter your Guess:")
        guess = guess.lower()
# this will add the letter that the user guessed to the already guessed pile so that in the future the user won't be able to guess that same letter again
    used_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct! You Guessed The Word!")

# New version of the word with both letters and dashes in them (because the user guessed some of the words)


        new_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_guess += guess
            else:
                new_guess += current_guess[letter]

        current_guess = new_guess
    else:
        print("Sorry that's not correct")

        incorrect_guess +=1

# Ending the Game (Either you guessed too many wrong and you lose or you guessed the entire word within the limit and you win)
if incorrect_guess == max_wrong:
    print(Hangman[6])
    print("Sorry, You Lost")
    print("The correct word is", word)

else:
    print("You Won!!")
    print("The word you guessed is", word)

