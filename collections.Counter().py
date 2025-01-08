from collections import Counter

if __name__ == "__main__":
    available_shoes = int(input())
    shoe_inventory = list(map(int, input().split()))
    stock_count = Counter(shoe_inventory)
    customer_count = int(input())
    revenue = 0

    for _ in range(customer_count):
        shoe_size, price = map(int, input().split())

        if stock_count[shoe_size] > 0:
            revenue += price
            stock_count[shoe_size] -= 1

    print(revenue)
