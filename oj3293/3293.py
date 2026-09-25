"""BigFrame"""

def main():
    """BigFrame"""
    lines = []
    for _ in range(5):
        line = input()
        lines.append(line.rstrip())
    max_len = max(len(line) for line in lines)
    max_len = max(max_len, 2)
    border = '*' * (max_len + 4)
    print(border)
    for line in lines:
        print(f"* {line.ljust(max_len)} *")
    print(border)
main()
