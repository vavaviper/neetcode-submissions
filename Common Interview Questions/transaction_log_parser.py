'''
Part 1: Parse the transactions

You are given a comma-separated string:

"txn1:100:USD,txn2:50:CAD,txn3:75:EUR"

Each transaction has the format:

txn_id:amount:currency

Write a function that parses the string into structured records.

For the example above, the expected result would be something like:

[
    {"txn_id": "txn1", "amount": 100, "currency": "USD"},
    {"txn_id": "txn2", "amount": 50, "currency": "CAD"},
    {"txn_id": "txn3", "amount": 75, "currency": "EUR"}
]

Question: How would you implement Part 1?
'''

def parser(transaction):
    output = []
    transaction = transaction.split(",")

    for t in transaction:
        t = t.split(":")
        t_id = t[0]
        amt = t[1]
        currency = t[2]

        output.append({"txn_id": t_id, "amount": amt, "currency": currency})
    return output

transaction = "txn1:100:USD,txn2:50:CAD,txn3:75:EUR"

print(parser(transaction))
transactions = parser(transaction)

'''
Part 2

Now, given the structured records from Part 1, return the total amount for each currency.

Example:

[
    {"txn_id": "txn1", "amount": 100, "currency": "USD"},
    {"txn_id": "txn2", "amount": 50, "currency": "CAD"},
    {"txn_id": "txn3", "amount": 75, "currency": "USD"}
]

Expected:

{"USD": 175, "CAD": 50}

How would you implement Part 2?
'''

transactions = [
    {"txn_id": "txn1", "amount": 100, "currency": "USD"},
    {"txn_id": "txn2", "amount": 50, "currency": "CAD"},
    {"txn_id": "txn3", "amount": 75, "currency": "USD"}
]

def currency_count(transactions):
    output = {}
    for t in transactions:
        amount = int(t["amount"])
        currency = t["currency"]

        if currency not in output:
            output[currency] = 0
        output[currency] += amount

    return output


print(currency_count(transactions))

'''
Part 3

Now we're adding exchange rates.

Given the transactions and an exchange-rate map where each rate represents 1 unit of that currency in USD:

rates = {
    "USD": 1.0,
    "CAD": 0.73,
    "EUR": 1.17
}

Calculate the grand total in USD.

For example:

transactions = [
    {"txn_id": "txn1", "amount": 100, "currency": "USD"},
    {"txn_id": "txn2", "amount": 50, "currency": "CAD"},
    {"txn_id": "txn3", "amount": 75, "currency": "EUR"}
]

The calculation is:

100 * 1.0
50 * 0.73
75 * 1.17

Return the grand total.

How would you implement Part 3?

'''
rates = {
    "USD": 1.0,
    "CAD": 0.73,
    "EUR": 1.17
}

transactions = [
    {"txn_id": "txn1", "amount": 100, "currency": "USD"},
    {"txn_id": "txn2", "amount": 50, "currency": "CAD"},
    {"txn_id": "txn3", "amount": 75, "currency": "EUR"}
]
target_currency = "USD"

def exchange(rates, transactions, target_currency):
    output = 0
    count = currency_count(transactions)

    #go through each currency in the currency count and convert any using the rates provided if not target
    for c in list(count.keys()):
        curr_currency = c
        curr_currency_count = count[c]

        if curr_currency == target_currency:
            output += curr_currency_count

        elif curr_currency != target_currency:
            rate = rates[curr_currency] / rates[target_currency]
            print(curr_currency, curr_currency_count, rate)
            output += rate * curr_currency_count

    return output

print(exchange(rates, transactions, target_currency))

