"""pod"""

def main():
    """find"""
    line = int(input())
    number = []
    for _ in range(line):
        num = int(input())
        number.append(num)
    
    min_number = number[0]
    for num in number:
        if num < min_number:
            min_number = num
    
    print(min_number)
main()
