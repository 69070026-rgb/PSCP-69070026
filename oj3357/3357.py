"""Giraffe"""

def main():
    """Giraffe"""
    n = int(input())
    g = []
    for _ in range(n):
        g.append(int(input()))
    count = 0
    for i in range(n):
        if n == 1:
            count = 1
            break
        if not i:
            if g[i] > g[i + 1]:
                count += 1
        elif i == n - 1:
            if g[i] > g[i - 1]:
                count += 1
        else:
            if g[i] > g[i - 1] and g[i] > g[i + 1]:
                count += 1
    print(count)
main()
