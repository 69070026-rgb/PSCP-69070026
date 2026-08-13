"""flash express"""

def main():
    flash = input().split()
    package = int(input())
    come = flash[0]
    out = flash[1]
    tax = {
        ("BKK","CNX") : 10 ,
        ("CNX","UBP") : 15 ,
        ("UBP","BKK") : 20 ,
        ("BKK","PKT") : 25 ,
        ("PKT","CNX") : 30 ,
        ("UBP","PKT") : 30
    }
    route = (come,out)
    pricefirst = tax.get(route)

    weight = { 
        10 : 30 ,
        15 : 40 ,
        20 : 40 ,
        25 : 50 ,
        30 : 60 ,
        40 : 70 
    }
    weight_price = weight.get(package,0)
    price = weight_price * package
    price += pricefirst
    print(price)
main()