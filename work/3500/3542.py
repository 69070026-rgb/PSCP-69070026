"""Calculator"""

def main():
    """Calculator"""
    n = int(input())
    if n == 1:
        print(1)
        return
    ans = 0
    digit = 1
    i = 1
    while i <= n:
        end = (i * 10) - 1
        if end > n:
            end = n
        cnt = (end - i) + 1
        ans += (cnt * digit)
        i *= 10
        digit += 1
    print(ans + n)
main()
