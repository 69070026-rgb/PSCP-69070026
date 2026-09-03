"""The sum of the greater values"""

def main():
    """The sum of the greater values"""
    number = int(input())
    max_values = []
    for _ in range (number):
        num1 = int(input())
        num2 = int(input())
        max_values.append(max(num1, num2))
    total = sum(max_values)
    final = " + ".join(map(str, max_values))
    print(f"{final} = {total}") 
main()
