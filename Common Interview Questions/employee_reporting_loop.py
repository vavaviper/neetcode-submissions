'''
Employee Reporting Loop

You are given a company’s employee reporting structure. Each employee reports directly to at most one other employee.

Implement a function that determines whether the reporting structure contains a loop.

Function
hasReportingLoop(reports)
Input

reports is a list of pairs:

[employee, manager]

where employee reports directly to manager.

Each employee and manager is represented by an integer ID.

Return

Return true if there is a reporting loop in the organization.

Otherwise, return false.

Examples

Example 1

Input:
[
  [1, 2],
  [2, 3],
  [3, 4]
]

Output:
false

There is a valid chain:

1 → 2 → 3 → 4

Example 2

Input:
[
  [1, 2],
  [2, 3],
  [3, 1]
]

Output:
true

The reporting structure contains a loop:

1 → 2 → 3 → 1

Example 3

Input:
[
  [1, 2],
  [2, 3],
  [4, 5]
]

Output:
false

There are multiple independent reporting chains, but neither contains a loop.

Constraints
1 ≤ reports.length ≤ 100,000
Employee IDs are positive integers.
An employee reports to at most one manager.
An employee may appear as a manager for multiple employees.

Don't worry about solving it yet. This is the kind of prompt where the implementation is relatively straightforward once you identify the underlying graph structure, but I won't give away the approach.
'''

def hasReportingLoop(reports):
    store = {}
    #create the dictionary with all the managers and reportings
    for employee, manager in reports:
        store[employee] = manager
    
    current_path = set()
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        if node in current_path:
            return True
        current_path.add(node)

        if node in store:
            if dfs(store[node]):
                return True
        current_path.remove(node)
        visited.add(node)
        return False
    for i in store:
        if dfs(i):
            return True
    return False
    
    
reports = [
    [1, 2],
    [2, 3],
    [3, 4]
]

# Expected: False
print(hasReportingLoop(reports))