"""LastStand"""
import json

def main():
    """LastStand"""
    n = json.loads(input())
    for num in n:
        print(str(num)[-1])
main()
