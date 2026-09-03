"""Prime numbers"""

def main():
    """find the Prime numbers"""
    num1, num2 = map(int, input().split())
    prime = []
    for i in range(num1, num2 + 1):
        if i > 1:
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if not i % j:
                    is_prime = False
                    break
            if is_prime:
                prime.append(i)
    if len(prime) > 0:
        print(" ".join(map(str, prime)))
    else:
        print("")
    print(f"Total primes: {len(prime)}")
main()
