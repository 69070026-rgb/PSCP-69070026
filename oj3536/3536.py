"""isPrime_large"""

def main():
    """isPrime_large"""
    n = int(input())
    if n <= 1:
        print("NO")
        return
    if n == 2:
        print("YES")
        return
    if not n % 2:
        print("NO")
        return
    for i in range(3, int(n**0.5) + 1, 2):
        if not n % i:
            print("NO")
            return
    print("YES")
main()
