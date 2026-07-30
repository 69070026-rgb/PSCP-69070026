"""Even and odd numbers"""

def main():
    """Count even and odd numbers"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num = [num1, num2, num3]
    even = 0
    odd = 0
    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(even)
    print(odd)
main()
