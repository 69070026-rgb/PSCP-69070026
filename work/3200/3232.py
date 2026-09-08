"""frog"""

def main():
    """frog"""
    x, y = map(int, input().split())
    jump = 0
    raya = 0
    while raya < y:
        if x <= 0:
           jump = -1
           break 
        raya += x
        x = x - 2
        jump += 1
    print(jump)
main()
