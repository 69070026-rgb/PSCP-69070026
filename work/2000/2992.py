"""suffle number"""

def main():
    """suffle"""
    number = input()
    sign = input()
    playback = int(number[::-1])
    numberconvert = int(number)
    if (10 <= numberconvert <= 99) and (sign == "+" ):
        print(f"{numberconvert} + {playback} = {numberconvert + playback}")
    elif (10 <= numberconvert <= 99) and (sign == "*" ):
        print(f"{numberconvert} * {playback} = {numberconvert * playback}")
    
main()
    
