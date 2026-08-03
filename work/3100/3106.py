"""ATM"""

def main():
    """ATM"""
    money = int(input())
    pun = money // 1000
    haroi = (money - (pun * 1000)) // 500
    roi = (money - (pun * 1000) - (haroi * 500)) // 100
    if money < 100 or money > 20000 or not money.is_integer():
        print("ERROR")
    if pun > 0:
        print(f"1000 = {pun}")
    if haroi > 0:
        print(f"1000 = {haroi}")
    if roi > 0:
        print(f"1000 = {roi}")
main()
