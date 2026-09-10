'''
You are given a list of transactions. Each transaction contains:

account_name: the account making the transaction
timestamp: when the transaction occurred
currency: the transaction currency
amount: the amount transferred

Transactions are provided in chronological order.

For each account, calculate its final balance for each currency.

Return all account/currency pairs whose final balance is non-zero.

Input
transactions = [
    ["acct_123", 1, "usd", 1000],
    ["acct_123", 2, "usd", 500],
    ["acct_321", 3, "usd", 400],
    ["acct_321", 4, "usd", -400]
]
Expected Output
[
    ["acct_123", "usd", 1500]
]

acct_321 is not included because its final USD balance is 0.

Constraints
1 <= len(transactions) <= 100,000
account_name is a non-empty string
currency is a lowercase string
amount is an integer
timestamp is an integer
Multiple currencies may exist for the same account.
Transactions for the same account/currency may appear multiple
'''

class Bank:
    def __init__(self):
        self.accounts = {}

    def transaction(self, input):
        name = input[0]
        timestamp = input[1]
        currency = input[2]
        amount = input[3]

        if name in self.accounts:
            self.accounts[name].balance += amount
        else:
            self.accounts[name] = Account(name, amount) 


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0