"""Left Arrow"""

def main():
    """Left Arrow"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for i in range(n):
        space = abs(i - mid)
        print(" " * space + "*" * k)
main()
