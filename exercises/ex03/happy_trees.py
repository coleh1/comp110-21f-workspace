"""Drawing forests in a loop."""

__author__ = "730400371"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

input: str = input("Depth: ")
number = int(input)
i: int = 0

while i < number:
    print((i + 1) * TREE)
    i = i + 1
