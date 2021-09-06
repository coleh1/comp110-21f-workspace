"""Repeating a beat in a loop."""

__author__ = "730400371"


beat: str = input("What beat do you want ot repeat? ")
repeat: str = input("How many times do you want to repeat it? ")
repeat_int = int(repeat)
i: int = 0
if repeat_int < 1:
    print("No beat...")
else:
    while i <= repeat_int:
        i = i + 1
    print(((beat + " ") * (repeat_int - 1)) + beat)