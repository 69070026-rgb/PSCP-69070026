"""AR TikTok"""

def main():
    """check if eye are in (x,y)"""
    r, x, y = map(float, input().split())
    if (x**2) + (y**2) < r**2:
        print("IN")
    elif (x**2) + (y**2) == r**2:
        print("ON")
    elif (x**2) + (y**2) > r**2:
        print("OUT")
main()
