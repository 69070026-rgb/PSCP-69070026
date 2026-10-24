"""Missing Numbers"""
def main():
    """Missing Numbers"""
    n = int(input())
    arr = set()
    while True:
        try:
            data = input().split()
            for val in data:
                num = int(val)
                if not num:
                    for i in range(1, n + 1):
                        if i not in arr:
                            print(i)
                    return
                arr.add(num)
        except EOFError:
            break
main()
