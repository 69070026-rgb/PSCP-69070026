"""Gifts and theft"""

def main():
    """Gifts and theft"""
    n, k, t = map(int, input().split())
    current = 1
    cycle = 1
    if current == t:
        print(cycle)
        return
    while True:
        current = (current - 1 + k) % n + 1
        if current == 1:
            break
        cycle += 1
        if current == t:
            break
    print(cycle)
main()
