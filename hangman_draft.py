import random


HANGMAN = [

""""
------
|    |
|
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|   -+-
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-
|
|
|
|
|
------
""",

""""
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   /
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   / \\
        |
|
------
"""
]


MAX_WRONG = len(HANGMAN) - 1

# The list of possible hangman words
#WORDS = <CODE HERE>

# Get a random word from our list of words -- hint: help(random.choice)
#word = <CODE HERE>

# Create a string that has one dash for each letter in the secret word
so_far = "-" * len(word)

# Create a variable to store the number of wrong guesses player has made
wrong = 0

#Create a list to store all the letters used
# used = <CODE HERE>


print "Welcome to Hangman. Good luck!"


while wrong < MAX_WRONG and so_far != word:
    # Print the current hangman
    #<CODE HERE>

    # Input the latest guess from the player.
    # guess = <CODE HERE>
    # Make sure we're forgiving with what was typed.
    # <CODE HERE>

    # Add the guess to the list of guesses.
    #<CODE HERE>

    if guess in word:
        print "Yes! {0} is in the word".format(guess)

        # Create the new "guessed so far" string.
        new = ""
        for i in range(0, len(word)):
            if guess == word[i]:
                new = new + guess
            else:
                new = new + so_far[i]
        so_far = new

    else:
        print "Sorry {0} is NOT in the word.".format(guess)
        # Increment the number of wrong guesses.
        # wrong = <CODE HERE>

    print
    print "So far, the word is: {0}".format(so_far)
    print "You've used the following letters:", ''.join(used)


if wrong == MAX_WRONG:
    print HANGMAN[wrong]
    print "You've been hanged!"

else:
    print "You guessed it!"

print "The word was {0}".format(word)

