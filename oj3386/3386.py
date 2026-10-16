"""Duplicate I"""

def main():
    """Duplicate I"""
    first = int(input())
    f = []
    second = int(input())
    s = []
    for _ in range(first):
        f.append(int(input()))
    for _ in range(second):
        s.append(int(input()))
    result = []
    for i in f:
        if i in s and i not in result:
            result.append(i)
    if result:
        result.sort(reverse=True)
        for h in result:
            print(h)
    else:
        print("Nope")
main()
