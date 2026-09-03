"""Gifts and theft"""

def main():
    """Gifts and theft"""
    n, k, t = map(int, input().split())
    current = 1
    cycle = 0
    if current == t:
        print(cycle)
        return
    while True:
        current = (current - 1 + k) % n + 1
        if current == 1:
            break
        cycle += 1
        if current == t:
            cycle += 1
            break
    print(cycle)
main()

