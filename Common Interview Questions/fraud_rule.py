'''
Fraud Rule Timeline Evaluation

You are given a timeline of fraud threshold changes for different merchants and a list of transactions.

Each rule change specifies:

a merchant_id
a timestamp
a new fraud threshold

Each transaction specifies:

a merchant_id
a timestamp
an amount

For each transaction, determine whether it should be flagged as fraudulent.

A transaction is fraudulent if its amount is greater than or equal to the threshold that was active for that merchant at the transaction's timestamp.

A threshold change becomes active starting at its timestamp.

If a merchant has no threshold defined before a transaction occurs, assume the transaction is not fraudulent.

Function Signature
def evaluate_transactions(rules, transactions):
    """
    rules: list of (merchant_id, timestamp, threshold)
    transactions: list of (merchant_id, timestamp, amount)

    Returns:
        list of booleans, one for each transaction
    """
Example
rules = [
    ("A", 10, 100),
    ("A", 20, 200),
    ("B", 15, 50),
]

transactions = [
    ("A", 5, 150),
    ("A", 10, 150),
    ("A", 15, 150),
    ("A", 20, 150),
    ("B", 16, 60),
]

Expected output:

[False, True, True, False, True]

Because:

Merchant A:
timestamp < 10   -> no threshold -> False
10 <= timestamp < 20 -> threshold 100 -> 150 is fraudulent
timestamp >= 20  -> threshold 200 -> 150 is not fraudulent

Merchant B:
timestamp >= 15 -> threshold 50 -> 60 is fraudulent
'''

def evaluate_transactions(rules, transactions):
    output = []

    rule_map = {}

    for r in rules:
        m_id = r[0]
        time = r[1]
        threshold = r[2]

        if m_id not in rule_map:
            rule_map[m_id] = []

        rule_map[m_id].append((time, threshold))

    for t in transactions:
        m_id = t[0]
        time = t[1]
        amount = t[2]

        if m_id not in rule_map:
            output.append(False)
            continue

        times = rule_map[m_id]

        active_threshold = None

        for rule_time, threshold in times:
            if rule_time <= time:
                active_threshold = threshold
            else:
                break

        if active_threshold is None:
            output.append(False)
        else:
            output.append(amount >= active_threshold)

    return output
                


rules = [
    ("A", 10, 100),
    ("A", 20, 200),
    ("B", 15, 50),
]

transactions = [
    ("A", 5, 150),
    ("A", 10, 150),
    ("A", 15, 150),
    ("A", 20, 150),
    ("B", 16, 60),
]

print(evaluate_transactions(rules, transactions))