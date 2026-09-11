'''
Email Subscription / Reminder System

You are building an email subscription management system.

Each subscription belongs to a user and a topic. A subscription has an expiry date and a notification schedule that determines when the user should receive a reminder.

For example, a subscription expiring on 2025-06-10 with a schedule of [-1] should send a reminder one day before expiry, on 2025-06-09.

A schedule may contain:

Numeric offsets, where -1 means one day before expiry, -7 means seven days before expiry, etc.
"start", which means the beginning of the subscription.
"end", which means the expiry date.

The system must support arbitrary numeric offsets and should not assume a fixed set of reminder types.

Requirements

Implement the following functions:

subscribe(user_id, topic_id, start_date, expiry_date, schedule)

Creates a subscription for the given user and topic.

user_id is an integer.
topic_id is an integer.
start_date and expiry_date are dates represented as integers in YYYYMMDD format.
schedule is a list containing numeric offsets and/or the strings "start" and "end".

Examples:

subscribe(1, 100, 20250601, 20250610, [-7, -1])
subscribe(2, 100, 20250601, 20250610, ["start", -1, "end"])

For the first subscription, reminders should be sent on:

20250603  # 7 days before expiry
20250609  # 1 day before expiry

For the second subscription:

20250601  # start
20250609  # 1 day before expiry
20250610  # end
send_schedule(current_date)

Checks all active subscriptions and sends all reminders that are scheduled for current_date.

For each reminder, output:

user_id topic_id

If a user has multiple subscriptions with reminders scheduled for the same date, send a reminder for each subscription.

The same user may therefore appear multiple times in the output.

Important Details
A subscription may have any number of schedule entries.
Numeric offsets can be any integer.
Do not hardcode specific offsets such as -1, -7, or -15.
"start" and "end" are special schedule values and should be handled separately from numeric offsets.
A reminder should only be sent once for a particular subscription and scheduled date.
Multiple subscriptions for the same user and topic should be treated as separate subscriptions.
Assume dates are valid and that current_date increases over time.
Example
subscribe(1, 100, 20250601, 20250610, [-7, -1])
subscribe(1, 200, 20250605, 20250610, ["end"])
subscribe(2, 100, 20250601, 20250610, ["start", -1])

send_schedule(20250601)

Output:

1 100
2 100

Then:

send_schedule(20250609)

Output:

1 100
2 100

And:

send_schedule(20250610)

Output:

1 200
'''
class EmailSubscription:
    def __init__(self):
        self.dates = {}

    def subscribe(self,user_id, topic_id, start_date, expiry_date, schedule):
        #find dates from schedule
        notifs = []
        for s in schedule:
            if s == "start":
                notifs.append(start_date)
            elif s == "end":
                notifs.append(expiry_date)
            else:
                notifs.append(int(expiry_date) + int(s))

        #add user_id and topic_id into dates dict with sendout as key
        for n in notifs:
            if n not in self.dates: 
                self.dates[n] = []
            self.dates[n].append(f"{user_id} {topic_id}")


    def send_schedule(self, date):
        print(self.dates)
        for i in self.dates[date]:
            print(i)


mail = EmailSubscription()
mail.subscribe(1, 100, 20250601, 20250610, [-7, -1])
mail.subscribe(1, 200, 20250605, 20250610, ["end"])
mail.subscribe(2, 100, 20250601, 20250610, ["start", -1])

mail.send_schedule(20250601)