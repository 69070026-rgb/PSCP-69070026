"""Season"""

def main():
    """season"""
    wt = 1, 2, 3
    sp = 4, 5, 6
    sm = 7, 8, 9
    fl = 10, 11, 12
    mounth = int(input())
    day = int(input())
    if (mounth in [3, 6, 9, 12]) and (day >= 21):
        if (mounth == 3):
            print("spring") 
        elif (mounth == 6):
            print("summer") 
        elif (mounth == 9):
            print("fall")
        elif (mounth == 12):
            print("winter")
    elif (mounth in [1, 2, 3]):
        print("winter")
    elif (mounth in [4, 5, 6]):
        print("spring")
    elif (mounth in [7, 8, 9]):
        print("summer")
    elif (mounth in [10, 11, 12]):
        print("fall")

main()
