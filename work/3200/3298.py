"""กระต่ายน้อยรัก BUU"""

def main():
    """กระต่ายน้อยรัก BUU"""
    text = input().strip()
    low = text.lower()
    a = len(low)
    if "buu" in low:
        max_u = 0
        for i in range(a):
            if low[i] == "b":
                count = 0
                for j in range(i + 1, a):
                    if low[j] == "u":
                        count += 1
                    else:
                        break
                if count > max_u:
                    max_u = count
        print(f"Yes {max_u}") 
    elif "b" in low:
        position = low.find("b")
        ans = text[:position + 1] + ('U' * (len(text) - position - 1))
        print(ans)
    else:
        length = len(text)
        repeat_buu = "BUU" * ((length // 3) + 1)
        print(repeat_buu[:length])
main()
