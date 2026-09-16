'''
14. Subscription Renewal / Event Flow

You are given a stream of subscription lifecycle events. Each event contains:

subscription_id: unique identifier for the subscription
event: one of "created", "renewed", "canceled", or "expired"
timestamp: integer representing when the event occurred

Each subscription follows this general lifecycle:

created starts an active subscription.
renewed extends an active subscription.
canceled ends the subscription.
expired ends the subscription.
Task

Implement:

process_events(events)

which processes the events and returns the current status and active date ranges for each subscription.

For each subscription, return:

{
    "status": "active" | "canceled" | "expired",
    "active_ranges": [(start_timestamp, end_timestamp), ...]
}

For an active subscription, the current active range should have None as its end timestamp.

Example

Input:

events = [
    ("sub1", "created", 10),
    ("sub1", "renewed", 20),
    ("sub1", "canceled", 30),
    ("sub2", "created", 15),
    ("sub2", "expired", 25)
]

Output:

{
    "sub1": {
        "status": "canceled",
        "active_ranges": [(10, 30)]
    },
    "sub2": {
        "status": "expired",
        "active_ranges": [(15, 25)]
    }
}
'''
def process_events(events):
    output = {}

    for e in events:
        sub_num = e[0]
        action = e[1]
        time = e[2]

        if sub_num not in output:
            output[sub_num] = {
                "status": None,
                "active_ranges": []
            }

        if action == "created":
            output[sub_num]["status"] = "active"
            output[sub_num]["active_ranges"].append((time, None))

        elif action == "renewed":
            output[sub_num]["status"] = "active"

        elif action == "canceled":
            output[sub_num]["status"] = "canceled"
            start = output[sub_num]["active_ranges"][-1][0]
            output[sub_num]["active_ranges"][-1] = (start, time)

        elif action == "expired":
            output[sub_num]["status"] = "expired"
            start = output[sub_num]["active_ranges"][-1][0]
            output[sub_num]["active_ranges"][-1] = (start, time)

    return output

events = [
    ("sub1", "created", 10),
    ("sub1", "renewed", 20),
    ("sub1", "canceled", 30),
    ("sub2", "created", 15),
    ("sub2", "expired", 25)
]
print(process_events(events))
    
