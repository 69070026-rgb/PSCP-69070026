"""coke"""

def main():
    """calculate new pro"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not d:
        print(0)
        return
    if not b:
        print(a * d)
        return
    caps = 0
    cap_gotten = 0
    price = 0
    while cap_gotten < d:
        need = d - cap_gotten
        if caps >= b:
            pro = min(caps // b, need)
            price += pro * c
            cap_gotten += pro
            caps = caps - pro * b + pro
        else:
            buy = min(need, b - caps)
            if buy <= 0:
                buy = need
            price += buy * a
            cap_gotten += buy
            caps += buy
    print(price)
main()
