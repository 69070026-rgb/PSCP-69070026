"""Classify"""
def main():
    """Classify"""
    dic = {}
    stop = False
    while not stop:
        try:
            arr = input().split()
            for w in arr:
                if w == "END":
                    stop = True
                    break
                yr = int(w[0:2])
                fac = int(w[2:4])
                if yr not in dic:
                    dic[yr] = {}
                if fac not in dic[yr]:
                    dic[yr][fac] = 0
                dic[yr][fac] += 1
        except EOFError:
            break   
    for yr in sorted(dic.keys()):
        chk = True
        for fac in sorted(dic[yr].keys()):
            if chk:
                print(f"{yr} {fac} {dic[yr][fac]}")
                chk = False
            else:
                print(f"-- {fac} {dic[yr][fac]}")
main()
