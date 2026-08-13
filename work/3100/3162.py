"""Multiplication table"""

def main():
    """Multiplication table"""
    number = int(input())
    i = 0
    multi = 0
    for i in range(1, 13):
       multi = number * i
       print(f"{number} * {i} = {multi}")
    i += 1
main()
