"""bill"""

def main():
    """bill"""
    Servicefee = 0.1
    vat = 0.07
    money = int(input())
    a = money*Servicefee
    b = (a + money)*vat
    if (500 <= money <= 10000):
        print(f"{(money + a + b):.2f}")
    elif money < 500:
        print(f"{(((money + 50)*vat) + (money + 50)):.2f}")
    elif money > 10000:
        print(f"{(((money + 1000)*vat) + (money + 1000)):.2f}")

main()
