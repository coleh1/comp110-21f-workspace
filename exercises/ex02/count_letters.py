"""Counting letters in a string."""

__author__ = "730400371"


letter1: str = input("What letter do you want to seach for?: ")
letter = str.lower(letter1)
word1: str = input("Enter a word: ")
word = str.lower(word1)
letters_inword = len(word) - 1
i: int = 0
letter_count: int = 0
a: int = 0
while i <= letters_inword:
    i = i + 1
    if word[a] == letter:
        a = a + 1
        letter_count = letter_count + 1
    else:
        a = a + 1
answer = str(letter_count)
print("Count: " + answer)