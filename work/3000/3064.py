"""birthday"""

def main():
    """check which friend was born first"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    if y1 < y2:
        print("1")
    elif y2 < y1:
        print("2")
    elif y1 == y2 and m1 == m2 and (d1 - d2) <=7:
        print("0")
main()
