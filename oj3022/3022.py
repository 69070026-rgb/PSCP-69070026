"""Temperature"""

def main():
    """convert Temperature"""
    tp = float(input())
    unit = input()
    convert = input()

    if unit == "C" and convert == "F":
        print(f"{(tp*1.8) + 32:.2f}")
    elif unit == "C" and convert == "K":
        print(f"{tp + 273.15:.2f}")
    elif unit == "C" and convert == "R":
        print(f"{(tp + 273.15)*1.8:.2f}")
    
    elif unit == "F" and convert == "C":
        print(f"{(tp - 32)/1.8:.2f}")
    elif unit == "F" and convert == "K":
        print(f"{((tp - 32)/1.8) + 273.15:.2f}")
    elif unit == "F" and convert == "R":
        print(f"{tp + 459.67:.2f}")
    
    elif unit == "K" and convert == "C":
        print(f"{tp - 273.15:.2f}")
    elif unit == "K" and convert == "F":
        print(f"{((tp - 273.15)*1.8) + 32:.2f}")
    elif unit == "K" and convert == "R":
        print(f"{tp * 1.8:.2f}")
    
    elif unit == "R" and convert == "C":
        print(f"{(tp - 491.67)/1.8:.2f}")
    elif unit == "R" and convert == "F":
        print(f"{tp - 459.67:.2f}")
    elif unit == "R" and convert == "K":
        print(f"{tp / 1.8:.2f}")
main()
