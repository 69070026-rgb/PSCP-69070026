"""Safe Password"""

def main():
    """safe"""
    character = input()
    number = int(input())
    passwordchar = "H"
    passwordnumber = 4567
    if (character == passwordchar) and (number == passwordnumber):
        print("safe unlocked")
    elif (character == passwordchar) and (number != passwordnumber):
        print("safe locked - change digit")
    elif (character != passwordchar) and (number == passwordnumber):
        print("safe locked - change char")
    else:
        print("safe locked")

main()
