"""grade"""

def main():
    """"""
    a = int(input())
    b = int(input())
    c = int(input())
    Total_score = a + b + c
    if Total_score >= 80:
        print("A")
    elif Total_score >= 75:
        print("B+")
    elif Total_score >= 70:
        print("B")
    elif Total_score >= 65:
        print("C+")
    elif Total_score >= 60:
        print("C")
    elif Total_score >= 55:
        print("D+")
    elif Total_score >= 50:
        print("D")
    else:
        print("F")
main()
