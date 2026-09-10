"""PickThemAgain"""

def main():
    """PickThemAgain"""
    num = list(map(int, input().split()))
    for i in reversed(num):
        if not i % 3 or not i % 5:
            print(i)
main()
