"""tiket"""

def main():
    """tiket"""
    seat = int(input())
    sold = 0
    while sold < seat:
        try:
            age, tickets = map(int, input().split())
        except EOFError:
            break
        if age < 15:
            print("-1")
            continue
        if sold + tickets > seat:
            print("-2")
            continue
        if 15 <= age <= 22:
            price = 120 * tickets
        elif age > 60:
            price = 75 * tickets
        else:
            price = 150 * tickets
        print(f"{price} {tickets}")
        sold += tickets
main()