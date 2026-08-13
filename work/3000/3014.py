"""Milk Promotion"""

def main():
    """Milk Promotion"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    total_bottle = d // a
    caps = total_bottle
    if b > 0:
        while caps >= b:
            rounds = caps // b
            new_bottle = rounds * c
            total_bottle += new_bottle
            caps = (caps % b) + new_bottle
    print(total_bottle)
main()
