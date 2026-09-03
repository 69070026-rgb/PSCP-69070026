"""Export products"""

def main():
    """Export products"""
    number = int(input())
    all_num = []
    even = 0
    odd = 0
    for _ in range (number):
        n = int(input())
        all_num.append(n)
        if n % 2:
            odd += 1
        elif not n % 2:
            even += 1
    total = sum(all_num)
    print(F"SUM {total}")
    print(F"EVEN {even}")
    print(F"ODD {odd}")
main()
