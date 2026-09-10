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

def tiered_cost(orders, rates):
    #create a rate map with all the rates and their costs at each tier
    '''
    {
    productA: {0:0,10:5, 50:3, 100:2}
    }
    '''
    rate_map = {}
    for r in rates:
        r = r.split(',')
        
        product_name = r[0]
        tier_start = r[1]
        tier_end = r[2]
        cost = r[3]

        if product_name in rate_map:
            rate_map[product_name][tier_end] = cost
        else:
            rate_map[product_name] = {}
            rate_map[product_name][tier_end] = cost
    print(rate_map)
    #find the product in the map
    for o in orders:
        o = o.split(",")
        order_num = o[0]
        country = o[1]
        product_name = o[2]
        quantity = int(o[3])

        keys = rate_map[product_name].keys()
        
        output = 0
        for k in keys:
            cost = rate_map[product_name][k]
            quantity -= int(k)
            if quantity > 0:
                output += int(k) * int(cost)
                print(output)
            if quantity < 0:
                quantity += int(k)
                output += int(quantity) * int(cost)
                print(output)
    return output

print(tiered_cost([
    "o1,US,productA,15",
    "o2,US,productA,60"
], [
    "productA,1,10,5",
    "productA,11,50,3",
    "productA,51,100,2"
]
))