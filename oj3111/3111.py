"""School cooperative"""

def main():
    """School cooperative"""
    status = input()
    amount = int(input())
    all_item = []
    for _ in range(amount):
        price = float(input())
        all_item.append(price)
    total_price = sum(all_item)
    if status == "Y":
        total_price = total_price - (total_price * (5/100))
    elif status == "N" and total_price >= 500:
        total_price = total_price - (total_price * (3/100))
    else:
        total_price = total_price
    total_price += 0.000001
    total_price = int((total_price * 100) + 0.5) / 100
    print(F"{total_price:.2f}")
main()
