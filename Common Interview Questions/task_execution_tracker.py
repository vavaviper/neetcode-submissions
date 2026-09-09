'''
Task Execution Tracker

You are building a system that manages a collection of tasks. Each task may depend on other tasks being completed before it can begin.

You are given a list of tasks and their dependencies.

A dependency [A, B] means that task A must be completed before task B can be started.

Implement:

getExecutionOrder(tasks, dependencies)

The function should return a valid order in which all tasks can be completed.

Requirements
Every task must appear exactly once in the returned list.
A task can only appear after all of its dependencies have been completed.
If multiple valid execution orders exist, return any valid order.
If it is impossible to complete all tasks because the dependencies contain a cycle, return an empty list.
Tasks may have no dependencies.
A task can depend on multiple other tasks.
The dependency list may contain tasks that are not explicitly listed in tasks.
Input

tasks

An array of strings representing the tasks.

dependencies

An array of pairs [A, B], where task A must be completed before task B.

Output

Return an array containing all tasks in a valid execution order.

If no valid execution order exists, return an empty array.

Example 1
tasks = ["Design", "Build", "Test"]

dependencies = [
    ["Design", "Build"],
    ["Build", "Test"]
]

Possible output:

["Design", "Build", "Test"]
Example 2
tasks = ["A", "B", "C", "D"]

dependencies = [
    ["A", "C"],
    ["B", "C"],
    ["C", "D"]
]

Possible output:

["A", "B", "C", "D"]

Another valid output:

["B", "A", "C", "D"]
Example 3
tasks = ["A", "B", "C"]

dependencies = [
    ["A", "B"],
    ["B", "C"],
    ["C", "A"]
]

Output:

[]
Function Signature
def getExecutionOrder(tasks, dependencies):
    # return a valid execution order

Expected difficulty: Medium-Hard
'''

def getExecutionOrder(tasks, dependencies):
    store = {} 
    degrees = {}  # of prereqs per task