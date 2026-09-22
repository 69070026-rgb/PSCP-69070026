"""Primary Color"""

def main():
    """Color"""
    primarycolor = {"Red","Yellow","Blue"}
    a = "Red"
    b = "Yellow"
    c = "Blue"
    firstcolor = input()
    secondcolor = input()
    if (firstcolor == a and secondcolor == b) or (firstcolor == b and secondcolor == a):
        print("Orange")
    elif (firstcolor == a and secondcolor == c) or (firstcolor == c and secondcolor == a):
        print("Violet")
    elif (firstcolor == b and secondcolor == c) or (firstcolor == c and secondcolor == b):
        print("Green")
    elif (firstcolor == secondcolor ) and firstcolor in primarycolor:
        print(firstcolor)
    else:
        print("Error")

main()
