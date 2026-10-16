"""CuteCat CuteFox"""

def main():
    """CuteCat CuteFox"""
    n = int(input())
    cat = {}
    fox = {}
    for _ in range(n):
        txt = input().strip()[1:-1].split(" : ")
        k = txt[0].strip()[1:-1]
        v = ":".join(txt[1:]).strip()[1:-1]
        if k.startswith("Cat") and k[3:].isdigit():
            cat[k] = v
        elif v.startswith("Cat") and v[3:].isdigit():
            cat[v] = k
        elif k.startswith("Fox") and k[3:].isdigit():
            fox[k] = v
        elif v.startswith("Fox") and v[3:].isdigit():
            fox[v] = k
    all_names = list(cat.values()) + list(fox.values())
    if "Cat01" not in cat and "Garfield" not in all_names:
        cat["Cat01"] = "Garfield"
    if "Fox01" not in fox and "Fubuki" not in all_names:
        fox["Fox01"] = "Fubuki"

    print(f"Cat : {len(cat)}")
    print(f"Fox : {len(fox)}")

    for k, v in sorted(cat.items(), key=lambda x: int(x[0][3:])):
        print(f"{v} : {k}")

    for k, v in sorted(fox.items(), key=lambda x: int(x[0][3:])):
        print(f"{v} : {k}")
main()
