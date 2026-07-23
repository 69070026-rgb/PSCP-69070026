"""national ID"""

def main():
    """check national ID"""
    national_id = input()
    if len(national_id) == 13:
        print("yes")
    else:
        print("no")
main()
