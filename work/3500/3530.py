"""SqFree"""
def main():
    """SqFree"""
    n = int(input())
    chk = [True] * (n + 1)
    tmp = int(n ** 0.5)
    for i in range(2, tmp + 1):
        sq = i * i
        for j in range(sq, n + 1, sq):
            chk[j] = False
    ans = 0
    for i in range(1, n + 1):
        if chk[i]:
            ans += 1
    print(ans)
main()
