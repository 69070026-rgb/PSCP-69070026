"""DigitV3"""
def main():
    """DigitV3"""
    dic = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    arr = input().split()
    ans = 0
    tmp = 0
    for i in arr:
        if i in dic:
            tmp += dic[i]
        elif i == "hundred":
            tmp *= 100
        elif i == "thousand":
            tmp *= 1000
            ans += tmp
            tmp = 0
    ans += tmp
    print(ans)
main()
