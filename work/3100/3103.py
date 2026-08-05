"""vovel"""

def main():
    """count vovel"""
    amout = int(input())
    vovel = ["A", "E", "I", "O", "U"]
    count = 0
    for i in range(amout):
        char = input().upper().strip()
        if char in vovel:
            count += 1
    print(count)
main()
