"""Guess a Random Number Game!"""

__author__ = "730400371"


from random import randint


points: int = 0
player: str = "a player"
face_emoji: str = ("\U0001F603")


def greet() -> None:
    """Greets the player."""
    print("Welcome to:'Can you guess what number I am thinking of'!")
    print(f"In this game, I (your intelligent computer) will pick a number and you will try to guess it {face_emoji}.")
    global player
    player = input("Player, remind me of your name? ")
    print(f"Oh yes, I remember now, your name is ({player}).")


def main() -> None:
    greet()
    global points
    print(f"You currently have ({points}) adventure points.")
    print(f"You have four options ({player})")
    print("Option 1 is to leave the game.")
    print("If you would like option 1, enter '1'")
    print("Option 2 is to play:'Can you guess what number I am thinking of,' with numbers from 1-10")
    print("If you would like option 2, enter '2'")
    print("Option 3 is to play:'Can you guess what number I am thinking of,' with numbers from 1-100")
    print("If you would like option 3, enter '3'")
    print("Option 4 allows you to gamble your current adventure points.  Gambling is risky, be careful!")
    print(f"You may gain more points or lose points.  You currently have ({points}) points to gamble")
    print("If you would like option 4, enter '4'")
    choice1: str = input("What option would you like? Please enter 1, 2, 3, or 4: ")
    choice = int(choice1)
    if choice == 1:
        goodbye()
    if choice == 2:
        game_1()
    if choice == 3:
        game_2()
    if choice == 4:
        gamble(points)
    if choice > 4:
        main()
    if choice < 1:
        main()


def goodbye() -> None:
    """Ends the game."""
    print(f"Goodbye ({player})")
    print("Thanks for playing!")
    print(f"You had ({points}) adventure points")
    print("GAME OVER")


def game_1() -> None:
    """A number guessing game from 1-10."""
    global points
    guesses = 0
    random_int: int = randint(0, 10)
    print("Welcome to: 'Can you guess what number I am thinking of,' with numbers from 1-10")
    guess1: str = input(f"({player}), guess a number between 1 and 10: ")
    guess = int(guess1)
    while random_int != guess:
        if guess > random_int:
            print("Wrong, guess lower.")
            guess1 = input("Guess again: ")
            guess = int(guess1)
            guesses = guesses + 1
            points = points + 1
        if guess < random_int:
            print("Wrong, guess higher.")
            guess1 = input("Guess again: ")
            guess = int(guess1)
            guesses = guesses + 1
            points = points + 1

    if random_int == guess:
        guesses = guesses + 1
        points = points + 1
        print("You guessed correctly!")
        print(f"The number was ({random_int})")
        print(f"It took you ({guesses}) guesses!")
        print(f"You have ({points}) adventure points")
        a: str = input("Please enter '1' to start over.  Enter any other value to end the game.")
        a_1 = int(a)
        if a_1 == 1:
            main()
        else:
            print("You did not enter 1.")
            goodbye()


def game_2() -> None:
    """A number guessing game from 1-100."""
    global points
    guesses = 0
    random_int1: int = randint(0, 100)
    print("Welcome to: 'Can you guess what number I am thinking of,' with numbers from 1-100")
    guess12: str = input(f"({player}), guess a number between 1 and 100: ")
    guess3 = int(guess12)
    while random_int1 != guess3:
        if guess3 > random_int1:
            print("Wrong, guess lower.")
            guess12 = input("Guess again: ")
            guess3 = int(guess12)
            guesses = guesses + 1
            points = points + 1
        if guess3 < random_int1:
            print("Wrong, guess higher.")
            guess12 = input("Guess again: ")
            guess3 = int(guess12)
            guesses = guesses + 1
            points = points + 1

    if random_int1 == guess3:
        points = points + 1
        guesses = guesses + 1
        print("You guessed correctly!")
        print(f"The number was ({random_int1})")
        print(f"It took you ({guesses}) guesses!")
        print(f"You have ({points}) adventure points")
        at: str = input("Please enter '1' to start over.  Enter any other value to end the game.")
        at_1 = int(at)
        if at_1 == 1:
            main()
        else:
            print("You did not enter 1.")
            goodbye()


def gamble(x: int) -> int:
    global points
    print(f"({player}) you have chosen to gamble your ({points}) adventure points. Good luck!")
    print("You can chose to gamble between -2 and 5 or -10 and 20")
    print("Whatever value you receive will be added to your score.")
    print("Enter '1' to gamble between -2 and 5.  Enter '2' to gamble between -10 and 20.  Enter 3 to exit")
    gambling1: str = input("Please enter a number: 1, 2, or 3: ")
    gambling = int(gambling1)
    if gambling == 1:
        y = randint(-2, 5)
        points = points + y
        print(f"You won ({y}) points.  You currently have ({points}) points!")
        main()
    if gambling == 2:
        y = randint(-10, 20)
        points = points + y
        print(f"You won ({y}) points.  You currently have ({points}) points!")
        main()
    if gambling == 3:
        main()
    if gambling > 3:
        print("You selected a number not equal to 1, 2, or 3.  Try again.")
        main()
    if gambling < 1:
        main()
        print("You selected a number not equal to 1, 2, or 3.  Try again.")
    return points    


if __name__ == "__main__":
    main()