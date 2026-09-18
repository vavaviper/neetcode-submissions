'''
Part 1: Parse the Shipping Costs

You are given a string containing shipping options:

"USD:CAD:DHL:5,USD:GBP:FEDEX:10,CAD:GBP:DHL:7"

Each entry has the format:

source:destination:carrier:cost

Write a function that parses this string and stores the shipping information in a data structure that can be queried later.

For example, you should be able to 
represent:

USD -> CAD -> DHL -> 5
USD -> GBP -> FEDEX -> 10
CAD -> GBP -> DHL -> 7

{
USD: [(CAD, DHL, 5), (GBP, FEDEX, 10)]
}

Question: What data structure would you use, and how would you implement the parsing?
'''

def shipping_cost_calc(input):
    input = input.split(",")
    output = {}

    for i in input:
        i = i.split(":")

'''
You could represent it as:

shipping = {
    "USD": [
        ("CAD", "DHL", 5),
        ("GBP", "FEDEX", 10)
    ],
    "CAD": [
        ("GBP", "DHL", 7)
    ]
}
Part 2: Look Up a Shipment

Given the data structure above and a shipment:

source = "USD"
dest = "GBP"
carrier = "FEDEX"

Return the shipping cost.

For this example, the answer would be:

10

Question: Write the function that performs this lookup.
'''


shipping = {
    "USD": [
        ("CAD", "DHL", 5),
        ("GBP", "FEDEX", 10)
    ],
    "CAD": [
        ("GBP", "DHL", 7)
    ]
}

def lookup(source, dest, carrier):
    source_countries = shipping[source]
    for s in source_countries:
        if s[0] == dest and s[1] == carrier:
            return s[2]
    return "not found"

print(lookup("USD", "GBP", "FEDEX"))

'''
Part 3: Cheapest Carrier

Now the carrier is not given.

Given:

source = "USD"
dest = "CAD"

Return the cheapest available carrier and its cost.

Example:

USD:CAD:DHL:5
USD:CAD:FEDEX:8
USD:CAD:UPS:6

Expected result:

("DHL", 5)

Question: How would you modify your lookup function to find the cheapest carrier?
'''

def cheapest(source, dest):
    if source not in shipping:
        return "source not found"

    cheapest_carrier = None
    cheapest_cost = float("inf")

    for s in shipping[source]:
        if s[0] == dest and s[2] < cheapest_cost:
            cheapest_carrier = s[1]
            cheapest_cost = s[2]

    if cheapest_carrier is None:
        return "not found"

    return cheapest_carrier, cheapest_cost

shipping = {
    "USD": [
        ("CAD", "DHL", 5),
        ("CAD", "FEDEX", 10)
    ],
    "CAD": [
        ("GBP", "DHL", 7)
    ]
}
print(cheapest("USD", "CAD"))

'''
Part 4: Multi-leg shipments

Now a shipment can have multiple legs.

For example:

USD -> CAD -> GBP

Using:

USD:CAD:DHL:5
CAD:GBP:DHL:7

the total cost is:

12

Question: Write a function that takes a list of countries like:

["USD", "CAD", "GBP"]

and returns the total cheapest cost for the entire route.
'''

def cheapest_route(countries):
    visited = {} #ask interviewer is countries can repeat, implement if yes with country: cheapest price
    price = 0
    for c in range(len(countries)-1):
        src = countries[c]
        dest = countries[c+1]
        if cheapest != "not found":
            price += cheapest(src, dest)[1]
        else:
            return "route invalid"
    return price

print(cheapest_route(["USD", "CAD", "GBP"]))