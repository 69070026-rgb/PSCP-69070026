"""Divisible"""

def main():
    """Check if the firstnum divisible by the secondnum"""
    first_num = int(input())
    second_num = int(input())
    if first_num % second_num == 0:
        print("yes")
    else:
        print("no")
main()
