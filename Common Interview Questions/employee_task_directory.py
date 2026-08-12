'''
Employee Task Dependencies

Your company has a set of tasks that need to be completed before a deployment.

Each task has a unique name. Some tasks depend on other tasks being completed first.

For example:

tasks = ["build", "test", "deploy", "lint"]

dependencies = [
    ["test", "build"],
    ["deploy", "test"],
    ["test", "lint"]
]

A dependency ["A", "B"] means B must be completed before A.

Implement:

getExecutionOrder(tasks, dependencies)

Return a valid order in which all tasks can be completed.

If no valid ordering exists, return an empty list.

Follow-ups
What if there is a circular dependency?
Can you detect a cycle?
Can you do this without repeatedly scanning all dependencies?
What is the time complexity?
'''