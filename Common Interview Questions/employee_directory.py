'''
Employee Directory

You are building a system that represents the reporting structure of a company.

Each employee has:

a unique employee ID
a name
a manager

The company structure forms a hierarchy. An employee may manage multiple employees, but each employee has at most one direct manager.

Implement a function:

getReports(employeeId)

that returns the names of all employees who directly or indirectly report to the given employee.

Input

You are given:

employees: a list of employee records
employeeId: the ID of the employee whose reports you want to find

Each employee record contains:

[employeeId, name, managerId]

where managerId is null for the CEO.

Output

Return a list containing the names of every employee who reports to employeeId, either directly or through another employee.

The order of the returned names does not matter.

Example

Input:

employees = [
    [1, "Alice", null],
    [2, "Bob", 1],
    [3, "Charlie", 1],
    [4, "David", 2],
    [5, "Emma", 2],
    [6, "Frank", 3]
]

employeeId = 1

Output:

["Bob", "Charlie", "David", "Emma", "Frank"]

Input:

employees = [
    [1, "Alice", null],
    [2, "Bob", 1],
    [3, "Charlie", 1],
    [4, "David", 2],
    [5, "Emma", 2],
    [6, "Frank", 3]
]

employeeId = 2

Output:

["David", "Emma"]
Constraints
1 <= number of employees <= 100,000
Employee IDs are unique.
Employee names are unique.
Every employee except the CEO has exactly one manager.
The reporting structure contains no cycles.
'''
from collections import deque

class Employee:
    def __init__(self, id, name, prev):
        self.id = id
        self.name = name
        self.prev = prev
        self.next = []

class Directory:
    def __init__(self, employees):
        self.employees = employees
        self.store = {}

        for i in employees:
            id, name, prev = i[0], i[1], i[2]
            self.store[id] = Employee(id, name, prev)

        for i in employees:
            id, name, prev = i[0], i[1], i[2]
            #add to managers {} of people who report to them
            if prev in self.store:
                self.store[prev].next.append(self.store[id])

    def getReports(self, employeeId):
        result = []

        def bfs(id):
            queue = deque()

            if id not in self.store:
                return
            
            queue += self.store[id].next
            
            print(queue)


            while queue:
                i = queue.popleft()
                result.append(i.name)
                queue += i.next

            

        bfs(employeeId)
        return result
        

directory1 = Directory([
    [1, "Alice", None],
    [2, "Bob", 1],
    [3, "Charlie", 1],
    [4, "David", 2],
    [5, "Emma", 2],
    [6, "Frank", 3]
])

print(directory1.getReports(1))
#should return ["Bob", "Charlie", "David", "Emma", "Frank"]