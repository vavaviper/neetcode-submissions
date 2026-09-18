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

def currency_conversion(rates, source, target):
    matrix = {}
    # create the adjacency matrix
    for r in rates:
        frm = r[0]
        to = r[1]
        amt = r[2]

        if frm not in matrix:
            matrix[frm] = []
        matrix[frm].append((to, amt))

        if to not in matrix:
            matrix[to] = []
        matrix[to].append((frm, 1/amt))

    # go follow through, have visited to avoid circular
    if source not in matrix:
        return "source not found"

    if target not in matrix:
        return "target not found"

    output = 1
    visited = set(source)
    q = []
    
    def traverse(source, target):
        if 
        return
        

    for m in matrix[source]:
        to = m[0]
        amt = m[1]
        visited.add(to)
        traverse(to)

