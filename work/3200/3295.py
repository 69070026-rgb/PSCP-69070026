"""Electric_Using"""

def main():
    """Electric_Using"""
    unit = int(input())
    price = 0
    ft = unit * 0.5
    while unit > 0:
        if unit <= 10:
            price += 5
            unit -= 1
        elif unit <= 50:
            price += 7
            unit -= 1
        elif unit <= 100:
            price += 10
            unit -= 1
        elif unit <= 200:
            price += 12
            unit -= 1
        elif unit > 200:
            price += 15
            unit -= 1
    vat = price * 0.07
    total = price + vat + ft
    print(f"{total:.1f}")
main()
