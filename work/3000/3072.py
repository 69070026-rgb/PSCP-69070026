"""vowel"""

def main():
    """count vowel"""
    name = input()
    a = name.count("a") + name.count("A")
    e = name.count("e") + name.count("E")
    i = name.count("i") + name.count("I")
    o = name.count("o") + name.count("O")
    u = name.count("u") + name.count("U")
    if a > 0:
        print(f"a : {str(a)}")
    if e > 0:
        print(f"e : {str(e)}")
    if i > 0:
        print(f"i : {str(i)}")
    if o > 0:
        print(f"o : {str(o)}")
    if u > 0:
        print(f"u : {str(u)}")
main()
