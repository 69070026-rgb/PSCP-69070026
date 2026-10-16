"""Shorten"""

def main():
    """Shorten"""
    f = []
    while True:
        n = int(input())
        if n == -1:
            break
        f.append(n)
    if not f:
        return
    result = []
    start = f[0]
    end = f[0]
    for i in f[1:]:
        if i == end + 1:
            end = i
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")

            start = i
            end = i

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    print(", ".join(result))
main()
