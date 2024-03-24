#This is hangman in Python

import random

words = ['apple', 'banana', 'elephant', 'guitar', 'pumpkin', 'dolphin', 'rainbow', 'chocolate', 'firefly', 'pineapple']

word = random.choice(words)
wordLength = len(word)
wordObscured = "_" * wordLength

incorrectGuesses = 0
guessMade = []

while incorrectGuesses <= 5:
    print(f"\nthe word looks like the following: {wordObscured}")

    if wordObscured == word:
        print(f"\ncongratulations, you have guessed the word {word} correctly with {incorrectGuesses} wrong guesses!")
        break

    guess = input("guess a letter to be in the word: ").lower()

    if guess in guessMade:
        print(f"you have already guessed the letter {guess}! You cannot guess this letter again, try another letter")
    else:
        for i in range(0, wordLength):
            if guess == word[i]:
                wordObscuredList = list(wordObscured)
                wordObscuredList[i] = guess
                wordObscured = "".join(wordObscuredList)
                print(f"oh nice! You guessed the letter {guess} correctly")

        if guess not in wordObscured:
            incorrectGuesses += 1
            print(f"unfortunately the leter {guess} was not in the word. You now have {incorrectGuesses} wrong guesses")
    guessMade.append(guess)

if wordObscured != word:
    print(f"\nthe closest you got was {wordObscured}\nthe word was: {word}")