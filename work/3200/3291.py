"""Right Arrow"""

def main():
    """Right Arrow"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for i in range(n):
        space = mid - abs(i - mid)
        print(" " * space + "*" * k)
main()
