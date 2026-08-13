"""Ink"""

def main():
    """Ink"""
    s, n = map(int, input().split())
    pi = 3.1416
    
    for _ in range(n):
        x, y = map(int, input().split())
        
        area = pi * (x * x + y * y)
        time = area / s
        time_int = int(time)
        
        if time > time_int:
            print(time_int + 1)
        else:
            print(time_int)
main()
