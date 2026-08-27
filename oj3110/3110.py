"""flash express"""

def main():
    flash = input().split()
    package = float(input())
    come = flash[0]
    out = flash[1]
    route = (come, out)
    tax = {
        ("BKK", "CNX") : (10, 30),
        ("CNX", "UBP") : (15, 40),
        ("UBP", "BKK") : (20, 40),
        ("BKK", "PKT") : (25, 50),
        ("PKT", "CNX") : (30, 60),
        ("UBP", "PKT") : (40, 70),
    }
    if route not in tax:
        print("Error")
        return

    base_fee, weight_fee = tax[route]
    price = base_fee + weight_fee * package
    print(price)
main()