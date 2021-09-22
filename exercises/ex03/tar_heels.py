"""An exercise in remainders and boolean logic."""

__author__ = "730400371"

number: str = input("Enter an int: ")
number_int = int(number)

if number_int % 14 == 0:
    print("TAR HEELS")
else:
    if number_int % 2 == 0:
        print("TAR")
    else:
        if number_int % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")