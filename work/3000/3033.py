"""Gift wrap"""

def main():
    """find range of gift wrap"""
    r, h, k = map(float, input().split())
    pi = 3.14
    paper_width =  (2 * pi * r) + k
    paper_length = h + (2 * r)
    print(f"{paper_length:.2f} {paper_width:.2f}")
main()
