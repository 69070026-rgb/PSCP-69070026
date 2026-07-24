"""all the same"""

def main():
    """check if number are all the same"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 == num2 == num3:
        print("all the same")
    elif num1 != num2 != num3:
        print("all different")
    else:
        print("neither")
main()
