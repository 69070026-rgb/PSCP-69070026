"""NO 13"""

def main():
    """NO 13"""
    num = input()
    d1 = int(num[0])
    d2 = int(num[1])
    d3 = int(num[2])
    d4 = int(num[3])
    d5 = int(num[4])
    first = 13
    sec = 0
    third = 0
    if d1 > 5:
        first = 9
    elif d2 > 5:
        first = 10
    elif d3 > 5:
        first = 11
    elif d4 > 5:
        first = 12
    elif d5 > 5:
        first = 14

    if num == num[::-1]:
        if d1 + d5 > 5:
            sec = 1
        elif d2 * d4 > 5:
            sec = 2
    else:
        if d1 // d5 > 5:
            sec = 1
        elif d2 - d5 > 5:
            sec = 2

    if (d1 + d2 + d3 + d4 + d5) > 25:
        third = 1
    elif (d1 * d2 * d3 * d4 * d5) > 55:
        third = 2
    print(f"{first}{sec}{third}")
main()
