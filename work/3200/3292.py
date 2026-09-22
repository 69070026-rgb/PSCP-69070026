"""Arrow"""

def main():
    """Arrow"""
    direct = input()
    n = int(input())
    for i in range(len(direct)):
        d = direct[i]
        for j in range(n):
            if d == 'R':
                space = " " * (2 * j)
            elif d == 'L':
                space = " " * (n - j - 1)

            star = "*" * (n - j)
            print(space + star)
        for j in range(n - 2, -1, -1):
            if d == 'R':
                space = " " * (2 * j)
            elif d == 'L':
                space = " " * (n - j - 1)
        
            star = "*" * (n - j)
            print(space + star)
        if i < len(direct) - 1:
            print()
main()
