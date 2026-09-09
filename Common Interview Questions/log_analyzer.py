'''
Access Log Analyzer

You are given a list of employee access records from a company's internal systems.

Each record contains:

an employee ID
a timestamp
the system they accessed

The records are given in chronological order.

An employee is considered suspicious if they access the system more than k times within any consecutive t minute period.

Function Description

Complete the function findSuspiciousEmployees.

The function should return a list of employee IDs that meet the suspicious activity criteria.

Parameters
records: a list of access records
k: the maximum allowed number of accesses
t: the time window in minutes

Each access record is represented as:

[employee_id, timestamp]

where timestamp is an integer representing the number of minutes since the start of the day.

Returns

Return the employee IDs that have suspicious activity, sorted in ascending order.

Constraints
1 ≤ len(records) ≤ 10^5
1 ≤ employee_id ≤ 10^9
0 ≤ timestamp ≤ 10^9
1 ≤ k ≤ 10^5
1 ≤ t ≤ 10^9
Records are sorted by timestamp.
Example

Input:

records = [
    [101, 10],
    [102, 12],
    [101, 15],
    [101, 18],
    [102, 20],
    [101, 21]
]

k = 2
t = 10

Output:

[101]

Explanation:

Employee 101 has more than 2 accesses within a 10 minute window, so they are flagged.

Employee 102 does not exceed the limit.
'''

class LogAnalyzer:
    def __init__(self, records, allowedLogins, timeLimit):
        self.records = records
        self.allowedLogins = allowedLogins
        self.timeLimit = timeLimit
        self.store = {}

        for i in records:


store = {101: [10, 15, 18, 21],
         102: [12, 20]}





