"""Point accumulation game"""

def main():
    """Point accumulation game"""
    number = int(input())
    point = 0
    for _ in range(number):
        n = input()
        if n == "+":
            point += 10
        elif n == "-":
            point -= 5
    print(point)
main()
