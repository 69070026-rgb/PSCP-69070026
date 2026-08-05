"""milk tea"""

def main():
    """Calculate the energy content of tea"""
    bubble, ambubble_input = input().split()
    tea, amsweet_input, amtea_input = input().split()
    ambubble = int(ambubble_input)
    amsweet = int(amsweet_input)
    amtea = int(amtea_input)
    if tea == "R":
        if amsweet == 1: tea_cal = 12
        elif amsweet == 2: tea_cal = 18
        elif amsweet == 3: tea_cal = 25
    elif tea == "T":
        if amsweet == 1: tea_cal = 15
        elif amsweet == 2: tea_cal = 20
        elif amsweet == 3: tea_cal = 30
    elif tea == "M":
        if amsweet == 1: tea_cal = 10
        elif amsweet == 2: tea_cal = 15
        elif amsweet == 3: tea_cal = 20
    if bubble == "H":
        bubble_cal = 5
    elif bubble == "O":
        bubble_cal = 3
    elif bubble == "J":
        bubble_cal = 2
    print((tea_cal*amtea) + (bubble_cal*ambubble))
main()
