"""increasing or decreasing"""

def main():
    """check increasing or decreasing"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 < num2 < num3:
        print("increasing")
    elif num1 > num2 > num3:
        print("decreasing")
    else:
        print("neither")
main()
