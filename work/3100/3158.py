"""Sum of Squares"""

def main():
    """Sum of Squares"""
    number = int(input())
    sum_of = 0
    for i in range (1, number + 1):
        sum_of += i**2
    print(sum_of)
main()
