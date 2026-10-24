"""iPhone 13 Again"""

def main():
    """iPhone 13 Again"""
    prices = {
        "iPhone 13 mini": {
            "128GB": 25900,
            "256GB": 29900,
            "512GB": 37900
        },
        "iPhone 13": {
            "128GB": 29900,
            "256GB": 33900,
            "512GB": 41900
        },
        "iPhone 13 Pro": {
            "128GB": 38900,
            "256GB": 42900,
            "512GB": 50900,
            "1TB": 58900
        },
        "iPhone 13 Pro Max": {
            "128GB": 42900,
            "256GB": 46900,
            "512GB": 54900,
            "1TB": 62900
        }
    }
    model = input().strip()
    storage = input().strip()
    storage = storage.replace(" ", "")

    if (model in prices) and (storage in prices[model]):
        print(prices[model][storage])
    else:
        print("Not Available")
main()
