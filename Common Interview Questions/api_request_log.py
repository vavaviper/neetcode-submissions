'''
API Request Log

You are working on an internal system that processes requests to a legacy API.

Each request is represented by a string containing:

a client ID
a timestamp
an endpoint

The system has a rule that limits how many requests a client can make within a given time window.

Given the request logs and the rate limit configuration, determine which requests should be accepted and which should be rejected.

Function Description

Implement:

processRequests(requests, windowSize, maxRequests)

where:

requests is an array of request records ordered by timestamp
windowSize is the size of the time window
maxRequests is the maximum number of requests a client can make within that window

Return an array indicating whether each request is accepted or rejected.

Input Format

The first line contains an integer n, the number of requests.

The next n lines each contain:

clientId timestamp

The final line contains two integers:

windowSize maxRequests
Output Format

Return n values, one for each request:

ACCEPT

if the request is allowed, and

REJECT

if the request exceeds the client's limit.

Example

Input

6
A 1
B 1
A 2
A 3
B 4
A 5
3 2

Output

ACCEPT
ACCEPT
ACCEPT
REJECT
ACCEPT
ACCEPT
Constraints
1 <= n <= 200,000
1 <= timestamp <= 10^9
1 <= windowSize <= 10^9
1 <= maxRequests <= n
Client IDs contain only alphanumeric characters.
Requests are provided in non-decreasing timestamp order.

Interview expectation: Aim for better than O(n²) time.
'''

class APIRequest:
    def __init__(self):
        return
    def processRequests(self, requests, windowSize, maxRequests):
        