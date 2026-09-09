"""lottory"""

def main():
    """lottory"""
    n1, n2 = input().split()
    n3, n4 = input().split()
    money = 0
    lek1, lek2 = int(n2), int(n4)
    if n1 == n3 and lek1 == lek2:
        money = 1000000
    elif lek1 == lek2:
        money = 100000
    elif n1 == n3 and lek1[2:4] == lek2[2:4]:
        money = 2000
    elif n1 == n3 and lek1[3:4] == lek2[3:4]:
        money = 1000
    elif lek1[2:4] == lek2[2:4]:
        money = 200
    elif lek1[3:4] == lek2[3:4]:
        money = 100
    elif n1 == n3:
        money = 20
    else:
        money = 0
    print(money)
main()
