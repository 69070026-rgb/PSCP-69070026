"""Bonus"""

def main():
    """calculate a bonus to company employee"""
    ps, age_input, sr_input = input().split()
    age = int(age_input)
    sr = int(sr_input)
    pm = 1500
    pb = 1000
    pg = 500
    if age < 5:
        if ps == "M":
            print(int(sr * (6/100) + pm))
        elif ps == "B":
            print(int(sr * (5/100)+ pb))
        elif ps == "G":
            print(int(sr * (4/100)+ pg))
    elif 5 <= age < 10:
        if ps == "M":
            print(int(sr * (8/100)+ pm))
        elif ps == "B":
            print(int(sr * (6/100)+ pb))
        elif ps == "G":
            print(int(sr * (5/100)+ pg))
    elif age > 10:
        if ps == "M":
            print(int(sr * (10/100)+ pm))
        elif ps == "B":
            print(int(sr * (7/100)+ pb))
        elif ps == "G":
            print(int(sr * (6/100)+ pg))
main()
