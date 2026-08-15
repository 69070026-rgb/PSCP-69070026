"""triangle"""

def main():
    """triangle"""
    num = int(input())
    for i in range(num + 1):
        for j in range(i):
            if j == i-1:
                print("0")
            elif not j or i == num:
                print("0",end="")
            else:
                print("1",end="")
main()
