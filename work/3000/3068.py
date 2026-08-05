"""leap year"""

def main():
    """calculate leap year"""
    year = int(input())
    if year > 1582:
        if not year % 4  and  year % 100 != 0:
            print("yes")
            if not year % 100:
                print("no")
            elif not year % 400:
                print("yes")
    elif year <= 1582:
        if not year % 4:
            print("yes")
        else:
            print("no")
main()
