"""sign"""

def main():
    """sign"""
    position = int(input())
    ans = ""
    for i in range(1, position + 1):
        if  i % 5 != 0:
            ans += "*"
        elif not i % 5:
            ans += "X"
    print(ans)
main()
