"""Fully pair"""

def main():
    """Fully pair"""
    text = input().strip()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    ans = []
    complete = set()
    for char in text:
        if counts[char] % 2 and char not in complete:
            ans.append(char)
            complete.add(char)
    if len(ans) > 0:
        print("".join(ans))
    else:
        print("fully paired")
main()
