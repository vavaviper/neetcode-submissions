'''
## 10. Currency Conversion (Graph-Style)

You are given a list of currency exchange rates represented as pairs of currencies and their exchange rate. For example:

```text
USD -> EUR: 0.9
EUR -> GBP: 0.85
USD -> CAD: 1.35
```

Implement a function that determines the conversion rate between two arbitrary currencies.

For example, given `USD` and `GBP`, the conversion rate can be calculated by traversing:

```text
USD -> EUR -> GBP
```

giving:

```text
0.9 * 0.85 = 0.765
```

If no conversion path exists between the two currencies, return `-1`.

Assume exchange rates can be traversed in both directions. For example, if:

```text
USD -> EUR = 0.9
```

then:

```text
EUR -> USD = 1 / 0.9
```

### Task

Implement:

```python
def conversion_rate(rates, source, target):
    ...
```

where `rates` contains the known exchange rates.

### Example

Input:

```text
rates = [
    ("USD", "EUR", 0.9),
    ("EUR", "GBP", 0.85),
    ("USD", "CAD", 1.35)
]

source = "USD"
target = "GBP"
```

Output:

```text
0.765
```

If:

```text
source = "USD"
target = "JPY"
```

Output:

```text
-1
```
'''

from collections import deque

def conversion_rate(rates, source, target):
    # make the dictionary of the rates
    rate_map = {}
    for r in rates:
        if r[0] not in rate_map:
            rate_map[r[0]] = []
        rate_map[r[0]].append((r[1], r[2]))
        if r[1] not in rate_map:
            rate_map[r[1]] = []
        rate_map[r[1]].append((r[0], 1/r[2]))

    #check if circular dependencies / possible
    rate = 1

    def traverse(source):
        q = deque()
        visited = []
        if source in rate_map:
            q.append(rate_map[source])
            visited.append(rate_map[source])
        for i in q:
            rate *= i[1]
            traverse(i[0]) 
            q.pop()
    traverse(source)