"""Flower bed"""

def main():
    """Flower bed"""
    l, n = map(int, input().split())
    m = 1
    while True:
        d = m * l
        total = d * (d + 1) // 2
        if total >= n:
            print(m)
            break
        m += 1
main()
