import random

def choose_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip()

def create_word_string(word, letters_guessed):
    word_string = ""
    for letter in word:
        if letter in letters_guessed:
            word_string += letter + " "
        else:
            word_string += "_ "
    return word_string

def get_guess(letters_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in letters_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

def play_hangman():
    word = choose_word()
    letters_guessed = []
    num_guesses = 0
    print("Let's play Hangman! The word has {} letters.".format(len(word)))
    while True:
        word_string = create_word_string(word, letters_guessed)
        print(word_string)
        if "_" not in word_string:
            print("Congratulations! You guessed the word {}".format(word))
            return
        guess = get_guess(letters_guessed)
        letters_guessed.append(guess)
        if guess not in word:
            num_guesses += 1
            print("Sorry, that letter is not in the word. You have {} guesses left.".format(6 - num_guesses))
        if num_guesses == 6:
            print("Sorry, you lost. The word was {}".format(word))
            return

play_hangman()
