"""box"""

def main():
    """box"""
    w, l, m, n = map(int, input().split())
    min_waste = w * l
    for i in range(m, n + 1):
        waste = (w % i) * (l % i)
        if waste < min_waste:
            min_waste = waste
        if min_waste == 0:
            break
    print(min_waste)
main()
