'''
3. Fraud / Anomaly Detection

You are given a stream of transactions and a fraud threshold for each merchant.

Each transaction is:

transaction_id, merchant_id, amount, currency, country

Each merchant is:

merchant_id, expected_currency, expected_country, min_amount, max_amount, fraud_threshold

For each transaction:

Validate that the transaction data is valid.
Extract these features:
currency matches expected
country matches expected
amount is within the expected range
Calculate the match ratio:
matched_features / total_features
If the ratio is below 50%, flag it as SUSPICIOUS.
Otherwise, return OK.

Example:

transactions = [
    "t1,m1,50,USD,US",
    "t2,m1,150,USD,US",
    "t3,m1,50,CAD,CA"
]

merchants = [
    "m1,USD,US,10,100,500"
]

Expected:

t1 OK
t2 OK
t3 SUSPICIOUS

Follow-up

Replace SUSPICIOUS with up to 2 specific error codes, in priority order:

CURRENCY_MISMATCH
COUNTRY_MISMATCH
AMOUNT_OUT_OF_RANGE

If there are no issues, return OK.

Variant: Instead of transactions, process CHARGE and DISPUTE events. Track each merchant's total disputed amount and mark the merchant FRAUDULENT once it reaches its fraud threshold.
'''
class Merchant:
    def __init__(self,merchant_id,expected_currency,expected_country,min_amount,max_amount,fraud_threshold):
        self.merchant_id = merchant_id
        self.expected_currency = expected_currency
        self.expected_country = expected_country
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.fraud_threshold = fraud_threshold

def fraud_detection(transactions, merchants):
    # make a dictionary of merchants and their features
    merchant_feats = {}
    for i in merchants:
        i = i.split(",")
        merchant_feats[i[0]] = Merchant(i[0], i[1], i[2], i[3], i[4], i[5])
        
    #go through each transaction
    errors = []
    for t in transactions:
        t = t.split(",")
        sus = 0
        id = t[1]
        currency = t[3]
        if merchant_feats[id].expected_currency != currency:
            sus += 1
            errors.append("CURRENCY_MISMATCH")
        country = t[4]
        if merchant_feats[id].expected_country != country:
            sus += 1
            errors.append("COUNTRY_MISMATCH")
        amt = t[2]
        if merchant_feats[id].min_amount <= currency or merchant_feats[id].max_amount >= currency:
            sus += 1
            errors.append("AMOUNT_OUT_OF_RANGE")
        #check feature ratio and if over 50% return ok, else the error
        if sus / 5 <= 0.5:
            print(id, "OK")
        else:
            print(id, " ".join(errors[0:2]))
        errors = []

fraud_detection( ["t1,m1,50,USD,US","t2,m1,150,USD,US","t3,m1,50,CAD,CA"],["m1,USD,US,10,100,500"])
