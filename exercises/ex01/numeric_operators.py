"""Numerical Operators Puzzle."""

__author__ = "730400371"

first_number: str = input("Pick a number from 1 to 10.")
second_number: str = input("Pick a second number from 1 to 10.")
print("Left-hand side: " + first_number)
print("Right-hand side: " + second_number)

int_first_number = int(first_number)
int_second_number = int(second_number)
answer1 = str(int_first_number ** int_second_number)
answer2 = str(int_first_number / int_second_number)
answer3 = str(int_first_number // int_second_number)
answer4 = str(int_first_number % int_second_number)
print(first_number + " ** " + second_number + " is " + answer1)
print(first_number + " / " + second_number + " is " + answer2)
print(first_number + " // " + second_number + " is " + answer3)
print(first_number + " % " + second_number + " is " + answer4)
