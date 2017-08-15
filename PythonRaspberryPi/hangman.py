# Hangman Game
#
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random

# constants
HANGMAN = (
'''
 ------
 |    |
 |
 |
 |
 |
 |
 |
----------
''',
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |    |
 | 
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   \|
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   \|/
 |   
 |   
 |   
 |     
----------
""",
"""
 ------
 |    |
 |    O
 |   \|/
 |    |
 |   
 |   
 |     
----------
""",
"""
 ------
 |    |
 |    O
 |   \|/
 |    |
 |   / 
 |   
 |      
----------
""",
"""
 ------
 |    |
 |    O
 |   \|/
 |    |
 |   / \
 |  
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("GOOGLE", "BING", "YAHOO", "WIKIPEDIA", "FACEBOOK", "INSTAGRAM")

# initialize variables
word = random.choice(WORDS)   # the word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed


print ("Welcome to Hangman.")
x = input ("Would you like to play? yes/no ")

if x == 'yes':
    while wrong < MAX_WRONG and so_far != word:
        print (HANGMAN[wrong])
        print ("\nUSED LETTERS:\n", used)
        print ("\nSo far, the word is:\n", so_far)

        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()
        
        while guess in used:
            print ("You've already guessed the letter:", guess)
            guess = input("Enter your guess: ")
            guess = guess.upper()

        used.append(guess)

        if guess in word:
            print ("Correct!", guess, "is in the word!")

            # create a new so_far to include guess
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]              
            so_far = new

        else:
            print ("Sorry,", guess, "isn't in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print (HANGMAN[wrong])
        print ("\nYou've been hung!")
    else:
        print ("\nYou won!")
        
    print ("The word was:", word)
else:
    print("Well, that's too bad")

input("\nPress the enter key to exit.")
