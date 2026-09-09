'''
# Exchange Network

You are building a system that tracks exchange rates between different currencies.

Each exchange rate is represented as a pair:

`[fromCurrency, toCurrency, rate]`

This means that **1 unit of `fromCurrency` can be exchanged for `rate` units of `toCurrency`**.

Implement a function:

`getExchangeRate(rates, fromCurrency, toCurrency)`

that returns the maximum exchange rate that can be obtained by converting from `fromCurrency` to 
toCurrency` through any sequence of available currency exchanges.

### Input

The function receives:

* `rates`: a list of exchange rate records, where each record contains:

  * a source currency
  * a destination currency
  * an exchange rate
* `fromCurrency`: the currency you are starting with
* `toCurrency`: the currency you want to obtain

You may use an exchange in either direction. If an exchange from `A` to `B` has rate `r`, then converting 
from `B` to `A` has rate `1 / r`.

### Output

Return the maximum possible exchange rate from `fromCurrency` to `toCurrency`.

If there is no valid sequence of exchanges connecting the two currencies, return `-1`.

### Constraints

* `1 <= rates.length <= 10^4`
* Currency names contain only uppercase English letters.
* Exchange rates are positive floating-point numbers.
* A currency may appear in multiple exchange pairs.
* `fromCurrency` and `toCurrency` may be the same currency.

### Example 1

Input:

```text
rates = [
    ["USD", "CAD", 1.4],
    ["CAD", "EUR", 0.65],
    ["USD", "EUR", 0.8]
]

fromCurrency = "USD"
toCurrency = "EUR"
```

Output:

```text
0.91
```

### Example 2

Input:

```text
rates = [
    ["USD", "CAD", 1.4],
    ["CAD", "GBP", 0.6],
    ["GBP", "EUR", 1.2]
]

fromCurrency = "USD"
toCurrency = "EUR"
```

Output:

```text
1.008
```

### Example 3

Input:

```text
rates = [
    ["USD", "CAD", 1.4]
]

fromCurrency = "USD"
toCurrency = "JPY"
```

Output:

```text
-1
```

### Function Signature

```python
def getExchangeRate(rates, fromCurrency, toCurrency):
    # return maximum exchange rate
```

**Note:** Your solution should handle large numbers of exchange pairs efficiently.

'''
class ExchangeNetwork:
    def __init__(self, rates):
        self.store = {}

        for from_currency, to_currency, rate in rates:
            if from_currency not in self.store:
                self.store[from_currency] = {}

            if to_currency not in self.store:
                self.store[to_currency] = {}

            self.store[from_currency][to_currency] = rate
            self.store[to_currency][from_currency] = 1 / rate

    def maxExchange(self, fromCurrency, toCurrency):
        if fromCurrency not in self.store or toCurrency not in self.store:
            return -1

        if fromCurrency == toCurrency:
            return 1

        max_rate = -1
        visited = set()

        def dfs(currency, current_rate):
            nonlocal max_rate

            if currency == toCurrency:
                max_rate = max(max_rate, current_rate)
                return

            visited.add(currency)

            for next_currency, rate in self.store[currency].items():
                if next_currency not in visited:
                    dfs(
                        next_currency,
                        current_rate * rate
                    )

            visited.remove(currency)

        dfs(fromCurrency, 1)

        return max_rate