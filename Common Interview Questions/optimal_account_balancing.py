'''
### Optimal Account Balancing
### 465. Optimal Account Balancing

You are given an array of transactions `transactions` where `transactions[i] = [from_i, to_i, amount_i]` indicates that the person with `ID = from_i` gave `amount_i` dollars to the person with `ID = to_i`.

Return the **minimum number of transactions required to settle the debt**.

### Example 1

```text
Input:
transactions = [[0,1,10],[2,0,5]]

Output:
2

0. -5
1. +10
2. -5



**Explanation:**

Person #0 gave person #1 $10.

Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is:

```text
Person #1 pays Person #0 $5
Person #2 pays Person #0 $5
```

### Example 2

```text
Input:
transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]

Output:
1
```

0. -4
1. +4
2. 


**Explanation:**

Person #0 gave person #1 $10.

Person #1 gave person #0 $1.

Person #1 gave person #2 $5.

Person #2 gave person #0 $5.

Therefore, person #1 only needs to give person #0 $4, and all debt is settled.

### Constraints

* `1 <= transactions.length <= 8`
* `transactions[i].length == 3`
* `0 <= from_i, to_i < 12`
* `from_i != to_i`
* `1 <= amount_i <= 100`

'''


def minTransfers(transactions):
    # find the debts
    debts = {}
    for t in transactions:
        frm = t[0]
        to = t[1]
        amt = t[2]

        if frm in debts:
            debts[frm] -= amt
        else:
            debts[frm] = -amt

        if to in debts:
            debts[to] += amt
        else:
            debts[to] = amt
    # try to settle
    for d in debts.keys():
        
