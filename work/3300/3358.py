"""pig"""

def main():
    """pig"""
    num = int(input())
    wg = list(map(int, input().split()))
    most = []
    for i in range(0, len(wg), 2):
        w1 = wg[i]
        w2 = wg[i + 1]
        most.append(max(w1, w2))
    change = list(map(str, most))
    equation = " + ".join(change)
    total = sum(most)
    print(f"{equation} = {total}")
main()
