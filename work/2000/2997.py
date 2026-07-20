"""Elo"""

def main():
    """asd"""
    RA = int(input())
    RB = int(input())
    team = str(input())
    EA = 1 / (1 + (10**((RB - RA) / 400)))
    EB = 1 / (1 + (10**((RA - RB) / 400)))
    if team == "A":
        print(round(EA,2))
    elif team == "B":
        print(round(EB,2))

main()