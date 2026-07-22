"""pod"""

def main():
    """find remaining stranded passengers"""
    n, k = map(int, input().split())
    passenger_count = [0] * (k + 1)
    for _ in range(n):
        line = int(input())
        passenger_count[line] += 1
    
    min_inline = min(passenger_count[1:])
    remaining = n - (min_inline * k)
    print(remaining)
main()
