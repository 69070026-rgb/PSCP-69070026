"""castle"""

def main():
    """Find the least possible way"""
    N = int(input())
    L = 1
    while L * L < N:
        L += 1
    p = N - (L - 1) ** 2

    if p % 2 == 1:
        print(2 * (L - 1))
    else:
        print(2 * L - 3)
main()
