'''
## 2. Payment-to-Invoice Reconciliation

Stripe's Invoicing product lets businesses send invoices to customers. Some payments need to be reconciled with open invoices based on the payment's memo line.

You're given:

- A payment string
- A list of invoice strings

```
payment = "payment5,1000,Paying off: invoiceC"
invoices = [
  "invoiceA,2024-01-01,100",
  "invoiceB,2024-02-01,200",
  "invoiceC,2023-01-30,1000"
]
```

**Task:** Parse the payment and invoices, find the invoice referenced in the memo line, and output a formatted reconciliation string.

Expected output: `payment5 pays off 1000 for invoiceC due on 2023-01-30`

*Note from a candidate report: be ready to generate your own input and write your own test cases (more than 2) — don't assume you'll just be handed a function signature and given test cases to run against.*
'''

def parsing(payment, invoices):
    # split up the string provided
    payment = payment.split(",")
    number = payment[0]
    amount = payment[1]
    looking_for = payment[2]

    #find the current invoice letter in the string
    curr_invoice = " "
    curr_invoice = looking_for.split()[-1]
    print(curr_invoice)

    #match that current invoice in the list of invoices
    for invoice in range(len(invoices)):
        i = invoices[invoice].split(",")

        print('"',i[0],'"','"', curr_invoice,'"')
        if i[0] == curr_invoice:
            date = i[1]
            return f'{number} pays off {amount} for {curr_invoice} due on {date}'

print(parsing("payment5,1000,Paying off: invoiceC",[
  "invoiceA,2024-01-01,100",
  "invoiceB,2024-02-01,200",
  "invoiceC,2023-01-30,1000"
]))




