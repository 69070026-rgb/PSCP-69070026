"""Conan"""

def main():
    """Conan"""
    text = input()
    position = int(input())
    ans = ""
    for char in text:
        if "a" <= char <= "z":
            change = chr(((ord(char) - ord("a") + position) % 26) + ord("a"))
            ans += change
        else:
            ans += char
    print(ans)
main()
