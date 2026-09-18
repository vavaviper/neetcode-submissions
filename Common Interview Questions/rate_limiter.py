'''
Part 1

You are building a rate limiter.

Given a stream of request events as (user_id, timestamp), implement:

is_allowed(user_id, timestamp)

A user can make at most N requests within any rolling 60-second window.

For example, if N = 3:

(1, 10)  -> allowed
(1, 20)  -> allowed
(1, 50)  -> allowed
(1, 55)  -> rejected
(1, 71)  -> allowed

[(1,10) (1,20) (1,50) (1,55) (1,71)]

Assume timestamps are integers and calls to is_allowed arrive in chronological order.

Question: How would you design the data structure and implement is_allowed?
'''

class RateLimiter:
    def __init__(self, N, requests):
        self.N = N
        self.requests = requests

    def is_allowed(self, user_id, timestamp):
        reqs = self.requests
        left = 0
        curr_n = 0

        # sliding window approach
        for right in range(len(reqs)):
            user = reqs[right][0]
            req_timestamp = reqs[right][1]

            # Ignore requests outside the rolling 60-second window
            if timestamp - req_timestamp >= 60:
                continue

            # Only count requests from this user
            if user == user_id:
                curr_n += 1

        if curr_n >= self.N:
            return "rejected"
        else:
            return "accepted"

    def time_until_next_allowed(self, user_id, timestamp):
        reqs = self.requests
        curr_n = 0

        for r in reqs:
            curr_user = r[0]
            curr_time = r[1]

            if curr_user != user_id:
                continue

            if timestamp - curr_time >= 60:
                continue

            curr_n += 1

            if curr_n >= self.limits[user_id]:
                return (curr_time + 60) - timestamp

        return 0

            


    



'''
Part 3

Add a helper:

time_until_next_allowed(user_id, timestamp)

It should return how many seconds the user has to wait before they can make another request.

For example, with a limit of 3:

(1, 10) -> allowed
(1, 20) -> allowed
(1, 50) -> allowed

time_until_next_allowed(1, 55)
-> 15

Because the request at 20 expires from the 60-second window at timestamp 80.

If the user can make a request immediately, return 0.

Question: How would you calculate the wait time?
'''