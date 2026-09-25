"""RGB mixed"""

def main():
    """RGB mixed"""
    chanal1 = list(map(int, input().split()))
    chanal2 = list(map(int, input().split()))
    red = (chanal1[0] + chanal2[0]) // 2
    green = (chanal1[1] + chanal2[1]) // 2
    blue = (chanal1[2] + chanal2[2]) // 2
    print(red, green, blue)
main()
