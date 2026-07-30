"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    list = []
    for i in range(A, B):
        if i % d == r:
            list.append(i)
    print(len(list))
main()
