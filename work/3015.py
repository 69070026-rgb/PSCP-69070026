"""Buffet promotion"""

def main():
    """promotion"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    payper = (z // x * y) + (z % x)
    price = payper * a
    print(price)

main()
