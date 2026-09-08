"""calculate point game"""

def main():
    """calculate point game"""
    base = int(input())
    bonus = int(input())
    stack = int(input())
    total_point = 0
    rating = 1
    special = 0
    multi = 0
    if stack > 3:
        total_point = round((base + bonus) * 1.5)
    else:
        total_point = base + bonus
    
    if total_point >= 1500:
        rating = 5
    elif total_point >= 1000:
        rating = 4
    elif total_point >= 500:
        rating = 3
    elif total_point >= 2000:
        rating = 2
    elif total_point < 200:
        rating = 1

    if rating == 5 and stack >= 7:
        special = 99
    elif rating == 4 and bonus > 300:
        special = 88
    print(total_point)
    print(rating)
    print(special)
main()
