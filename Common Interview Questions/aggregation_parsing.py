'''
13. Settlement & Aggregation Processing

You are given a stream of individual transactions across multiple accounts. Each transaction contains an account ID, transaction amount, date, and transaction ID.

Your task is to process the transactions and generate a daily settlement summary for each account.

A transaction is valid if:

account_id is not empty
amount is greater than 0
transaction_id is unique
date is in the format "YYYY-MM-DD"

Valid transactions should be included in the settlement total and transaction count for their account and date.

Invalid transactions should not be included in the settlement total, but should be recorded in the list of failed transactions along with the reason they failed validation.

Input

A list of transactions, where each transaction is represented as:

(transaction_id, account_id, amount, date)
Output

Return a dictionary where each key is a date and each value contains the settlement information for that date and account.

Each settlement should contain:

{
    "total": <sum of valid transaction amounts>,
    "count": <number of valid transactions>,
    "failed": <list of failed transaction IDs and reasons>
}
Example
transactions = [
    ("t1", "A", 100.00, "2026-09-15"),
    ("t2", "A", 50.00, "2026-09-15"),
    ("t3", "B", 200.00, "2026-09-15"),
    ("t4", "A", -20.00, "2026-09-15"),
    ("t5", "", 75.00, "2026-09-15"),
    ("t1", "B", 30.00, "2026-09-15"),
]

Expected output:

{
    "2026-09-15": {
        "A": {
            "total": 150.00,
            "count": 2,
            "failed": [
                ("t4", "invalid amount"),
                ("t5", "invalid account")
            ]
        },
        "B": {
            "total": 200.00,
            "count": 1,
            "failed": [
                ("t1", "duplicate transaction")
            ]
        }
    }
}

Function Signature
def process_settlements(transactions):
    pass
Constraints
1 <= len(transactions) <= 100,000
Transaction IDs may appear more than once.
Transactions may be provided in any order.
Multiple accounts may have transactions on the same date.
A transaction should only be counted once, even if its ID appears multiple times.

'''

from datetime import datetime

def process_settlements(transactions):
    old_trans = set()
    output = {}
    for t in transactions:
        transaction_id = t[0] 
        account_id = t[1] 
        amount = t[2] 
        date = t[3]

        if account_id not in output:
            output[account_id] = {"total": 0, "count": 0, "failed": []}
        

        if len(account_id) <= 0:
            output[account_id]["failed"].append((transaction_id, "invalid account"))
        elif int(amount) <= 0:
            output[account_id]["failed"].append((transaction_id, "invalid amount"))
        elif transaction_id in old_trans:
            output[account_id]["failed"].append((transaction_id, "duplicate transaction"))
        elif not datetime.strptime(date, "%Y-%m-%d"):
            output[account_id]["failed"].append((transaction_id, "incorrect date"))
        else:
            old_trans.add(transaction_id)
            output[account_id]["total"] += amount
            output[account_id]["count"] += 1
    return output

transactions = [
    ("t1", "A", 100.00, "2026-09-15"),
    ("t2", "A", 50.00, "2026-09-15"),
    ("t3", "B", 200.00, "2026-09-15"),
    ("t4", "A", -20.00, "2026-09-15"),
    ("t5", "", 75.00, "2026-09-15"),
    ("t1", "B", 30.00, "2026-09-15"),
]

print(process_settlements(transactions))