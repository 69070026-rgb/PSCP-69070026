"""calculator"""

def main():
    """calculator"""
    n = int(input())

    if n == 1:
        print("1")
    
    total_presses = 0
    length = 1
    start = 1
    while start <= n:
        end = (start * 10) - 1
        if end > n:
            end = n

        count_inrange = end - start + 1
        total_presses += count_inrange * length
        start *= 10
        length += 1
    total_presses += n
    print(total_presses)
main()
