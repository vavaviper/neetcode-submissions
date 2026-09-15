'''
12. CSV/Log Parsing + Validation + Matching

You are given a list of CSV-like transaction records and a second list containing expected transactions.

Each raw record has the format:

transaction_id,user_id,amount,currency,status

Implement:

def reconcile_records(raw_records, expected_records):

Your function should:

Parse each raw record.
Mark records as invalid if fields are missing, malformed, or violate validation rules.
Match valid records to expected_records using transaction_id.
Classify records as matched, mismatched, unmatched, or missing.

Validation rules:

Exactly 5 fields
transaction_id and user_id must be non-empty
amount must be a positive number
currency must be USD or CAD
status must be PENDING, COMPLETED, or FAILED

Return the IDs grouped by category, plus the invalid raw records.

Interviewer follow-up: What is the time complexity? How would you handle millions of records?
'''
def reconcile_records(raw_records, expected_records):
    # Turn expected records into a dictionary for quicker search
    transactions = {}
    check_missing = set()

    output = {
        "invalid": [],
        "matched": [],
        "mismatched": [],
        "unmatched": [],
        "missing": []
    }

    for e in expected_records:
        transactions[e["transaction_id"]] = e
        check_missing.add(e["transaction_id"])

    # Parse each raw record
    for r in raw_records:
        r_raw = r
        r = r.split(",")

        # Make sure the record has all 5 fields
        if len(r) != 5:
            output["invalid"].append(r_raw)
            continue

        transaction_id = r[0]
        user_id = r[1]
        amount = r[2]
        currency = r[3]
        status = r[4]

        # Validate the record
        if not transaction_id or not user_id:
            output["invalid"].append(r_raw)
            continue

        try:
            amount = float(amount)
        except ValueError:
            output["invalid"].append(r_raw)
            continue

        if amount <= 0:
            output["invalid"].append(r_raw)
            continue

        if currency not in ["USD", "CAD"]:
            output["invalid"].append(r_raw)
            continue

        if status not in ["PENDING", "COMPLETED", "FAILED"]:
            output["invalid"].append(r_raw)
            continue

        # Check whether this transaction was expected
        if transaction_id not in transactions:
            output["unmatched"].append(transaction_id)
            continue

        # Get the expected transaction
        current = transactions[transaction_id]

        # We've seen this expected transaction, so it isn't missing
        check_missing.discard(transaction_id)

        # Compare the fields
        if (
            current["user_id"] == user_id
            and current["amount"] == amount
            and current["currency"] == currency
            and current["status"] == status
        ):
            output["matched"].append(transaction_id)

        else:
            output["mismatched"].append(transaction_id)

    # Anything still in the set was expected but never received
    output["missing"] = list(check_missing)

    return output

raw_records = [
    "T001,U100,25.50,USD,COMPLETED",
    "T002,U101,100.00,USD,PENDING",
    "T003,U102,-5.00,USD,COMPLETED",
    "T004,U103,abc,USD,COMPLETED",
    "T005,U104,75.00,CAD,COMPLETED",
    "T006,U105,50.00,USD"
]

expected_records = [
    {"transaction_id": "T001", "user_id": "U100", "amount": 25.50, "currency": "USD", "status": "COMPLETED"},
    {"transaction_id": "T002", "user_id": "U101", "amount": 100.00, "currency": "USD", "status": "COMPLETED"},
    {"transaction_id": "T005", "user_id": "U104", "amount": 75.00, "currency": "CAD", "status": "COMPLETED"},
    {"transaction_id": "T007", "user_id": "U106", "amount": 20.00, "currency": "USD", "status": "COMPLETED"}
]

print(reconcile_records(raw_records, expected_records))