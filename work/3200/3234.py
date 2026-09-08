"""cristmas light"""

def main():
    """cristmas light"""
    light, total = input().split()
    total = int(total)
    colors = ["Red", "Green", "Blue"]
    start_index = 0
    if light == "R":
        start_index = 0
    elif light == "G":
        start_index = 1
    elif light == "B":
        start_index = 2
    final = []
    for i in range(total):
        current = (start_index + i) % 3
        final.append(colors[current])
    print(" ".join(final))
main()
