"""HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    s = input()
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 0
        dic[c] += 1
    arr = sorted(dic.keys(), key=lambda x: (x.isupper(), x))
    for k in arr:
        v = dic[k]
        tmp = ["-----"] * (v // 5)
        if v % 5:
            tmp.append("-" * (v % 5))

        ans = "|".join(tmp)
        print(f"{k} : {ans}")
main()
