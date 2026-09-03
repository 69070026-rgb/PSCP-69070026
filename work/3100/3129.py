"""Analyze coffee shop sales figures"""

def main():
    """Analyze coffee shop sales figures"""
    number = int(input())
    all_sale = []
    max_sale = 0
    min_sale = 0
    for _ in range (number):
        n = int(input())
        all_sale.append(n)
    total = sum(all_sale)
    max_sale = max(all_sale)
    min_sale = min(all_sale)
    avg = total / number
    print(total)
    print(max_sale)
    print(min_sale)
    print(round(avg, 1))
main()
