'''
## 4. Shipping Cost Lookup

You are given a string containing shipping routes. Each route contains:

origin, destination, carrier, cost

Routes are separated by `:`.

Example:

routes = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"

Given an origin country and destination country, return the shipping cost for that route.

Example:

routes = "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"

origin = "US"
destination = "CA"

Expected output:

3

If no route exists, return `-1`.

'''

def shipping_cost(routes, origin, destination):
    routes = routes.split(":")
    for r in routes:
        r = r.split(",")
        r_origin = r[0]
        r_destination = r[1]
        r_carrier = r[2]
        r_cost = r[3]

        if r_origin == origin and r_destination == destination:
            return r_cost
    return -1

print(shipping_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "CA"))
'''
test cases i would add
2 working
route does not exist
incorrect formats
locations exist but not direct route
'''



