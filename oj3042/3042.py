"""Divisible by 10"""

def main():
    """Find a number that is divisible by 10"""
    number = int(input())

    for i in range(number ,-1 ,-1):
        if i % 10 == 0:
            print(i, end = " ")
main()
