"""Work-Life Balance"""

def main():
    """Work-Life Balance"""
    num = int(input())
    heavy = 0
    light = 0
    for i in range(num):
        hours = int(input())
        if hours > 18:
            heavy += 1
        else:
            light += 1
    if heavy > 0:
        need = heavy - 1
    else:
        need = 0
    rest = 0
    if need > light:
        rest = need - light
    total = num + rest
    print(total)
main()
