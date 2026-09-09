"""X-shape"""

def main():
    """X-shape"""
    n1, n2 = input().split()
    num = int(n1)
    center = num // 2
    for i in range(num):
        for j in range(num):
            if i == j or i + j == num - 1:
                if n2 == "#":
                    print("#", end="")
                else:
                    laya = abs(i - center)
                    char =chr(ord(n2) + laya)
                    print(char, end="")  
            else:
                print("-", end="")
        print()
main()
