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

'''
each transaction includes p1 ->, p2, amount
you want to settle the debt with the least # of transactions
'''

def minTransactions(transactions):
    # go through each transactions and find the exact debt
    debts = {}
    output = 0
    for t in transactions:
        p1 = t[0]
        p2 = t[1]
        amt = t[2]

        if p1 not in debts:
            debts[p1] = 0
        if p2 not in debts:
            debts[p2] = 0
        debts[p1] -= amt
        debts[p2] += amt

    # have 2 sorted listed, 1 for ppl in debt and vice versa
    sorted_debts = dict(sorted(debts.items(), key=lambda item: item[1]))

    left = 0
    right = len(sorted_debts.keys()) - 1
    keys = list(sorted_debts.keys())
    print(keys)
    while left < right:
        # person with least debt
        least = sorted_debts[keys[left]]
        print(least)
        # person with most debt
        most = sorted_debts[keys[right]]
        print(most)

        if least == 0 and most == 0:
            return output

        if (least + most) == 0:
            least = 0
            most = 0
            left += 1
            right -= 1
            output += 1
        elif (least + most) > 0:
            least = least + most
            most = 0
            output += 1
            right -= 1
        elif (least + most) < 0:
            least = 0
            most = least + most
            output += 1
            left += 1
    return output

transactions = [[0,1,10],[2,0,5]]

print(minTransactions(transactions))