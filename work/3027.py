"""rabbit barb"""

def main():
    """barb"""
    x, y, z = map(int, input().split())
    priceper = int(input())
    lenge = (2*(x + y))*z
    price = lenge*priceper
    print(lenge)
    print(price)

main()
