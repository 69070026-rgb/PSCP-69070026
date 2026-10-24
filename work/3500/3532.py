"""GCD"""
def main():
    """GCD"""
    a = abs(int(input()))
    b = abs(int(input()))
    while b:
        tmp = a % b
        a = b
        b = tmp
    print(a)
main()
