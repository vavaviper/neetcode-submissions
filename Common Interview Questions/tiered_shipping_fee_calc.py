'''
5. Tiered Shipping Fee Calculation

You are given a list of orders and shipping rates for each product.

Each order is:

order_id, country, product, quantity

Each product has tiered shipping rates:

product, tier_start, tier_end, price_per_unit

The pricing tiers are applied progressively. For example:

productA,1,10,5
productA,11,50,3
productA,51,100,2

An order for 15 units costs:

10 * 5 + 5 * 3 = 65

An order for 60 units costs:

10 * 5 + 40 * 3 + 10 * 2 = 190

Task:

Calculate the total shipping cost for all orders.

Example:

orders = [
    "o1,US,productA,15",
    "o2,US,productA,60"
]

rates = [
    "productA,1,10,5",
    "productA,11,50,3",
    "productA,51,100,2"
]

Expected output:

255
'''
def shipping_fee_calc(orders, rates):
    rate_map = {}

    for r in rates:
        r = r.split(",")

        product = r[0]
        start = int(r[1])
        end = int(r[2])
        price = int(r[3])

        if product not in rate_map:
            rate_map[product] = []

        rate_map[product].append((start, end, price))

    # Make sure tiers are processed in order
    for product in rate_map:
        rate_map[product].sort()

    total = 0

    for o in orders:
        o = o.split(",")

        product = o[2]
        quantity = int(o[3])

        if product not in rate_map:
            return "product not found"

        for start, end, price in rate_map[product]:

            if quantity <= 0:
                break

            tier_size = end - start + 1

            if quantity >= tier_size:
                total += tier_size * price
                quantity -= tier_size
            else:
                total += quantity * price
                quantity = 0

    return total
        
orders = [
    "o1,US,productA,15",
    "o2,US,productA,60"
]

rates = [
    "productA,1,10,5",
    "productA,11,50,3",
    "productA,51,100,2"
]

print(shipping_fee_calc(orders, rates))


'''
good cases: multiple products, 1 products

bad cases: invalid products, past the last tier, negative numbers

edge cases: past the last tier, 
'''