"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400371"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
fortune_number = (randint(1, 4))
if fortune_number == 1:
    print("You will win the lottery this year.")
else:
    if fortune_number == 2:
        print("Today, you will meet your true love.")
    else:
        if fortune_number == 3:
            print("This is your lucky day.")
        else:
            if fortune_number == 4:
                print("You will have a year of good health.")
print("Now, go spread positive vibes!")