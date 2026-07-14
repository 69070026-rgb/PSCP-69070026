"""bill"""

def main():
    """bill"""
    Servicefee = 0.1
    vat = 0.07
    money = int(input())
    a = money*Servicefee
    b = (a + money)*vat
    if (500 <= money <= 10000):
        print(money + b)

main()
