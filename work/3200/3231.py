"""Guess the dice"""

def main():
    "Guess the dice"
    g = int(input())
    r = int(input())
    dice = [1, 2, 3, 4, 5, 6]
    if g not in dice:
        print("Invalid")
    elif g in dice:
        if g != r:
            print("Wrong!")
        elif g == r:
            print("Correct!")
main()
