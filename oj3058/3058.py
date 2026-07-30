"""BrickBridge"""

def main():
    """Bridge-building program"""
    a = int(input())
    b = int(input())
    goal = int(input())
    b_use = min(b, goal // 5)
    a_use = goal - (b_use * 5)
    if a >= a_use:
        print(a_use)
    else:
        print(-1)
main()
