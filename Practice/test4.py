""""""

def main():
    """"""
    tp = float(input())
    unit = input()
    convert = input()
    celsius = 0.0
    result = 0.0

    if unit == "C":
        celsius = tp
    elif unit == "F":
        celsius = (tp - 32) / 1.8
    elif unit == "K":
        celsius = tp - 273.15
    elif unit == "R":
        celsius = (tp - 491.67) / 1.8

    if convert == "C":
        result = celsius
    elif convert == "F":
        result = celsius * 1.8 + 32
    elif convert == "K":
        result = celsius + 273.15
    elif convert == "R":
        result = (celsius + 273.15) * 1.8

    print(f"{result:.2f}")
main()
