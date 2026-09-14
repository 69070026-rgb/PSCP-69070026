"""Teaching schedule"""

def main():
    """Teaching schedule"""
    n = int(input())
    a = int(input())
    time = n * a
    hour = time // 60
    minute = time % 60
    if hour and minute:
        print(f"{hour} hours {minute} minute")
    elif not minute:
        print(f"{hour} hours")
    elif not hour:
        print(f"{minute} minute")
main()
