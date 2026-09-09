'''
Workflow Deployment Manager

You are building a system that manages deployments for a software company.

Each deployment consists of several tasks. A task can only begin after all of its required prerequisite tasks have been completed.

Implement a class called DeploymentManager that determines a valid order in which all deployment tasks can be completed.

Class Requirements

Implement the following:

DeploymentManager(tasks)

Initializes the system with a list of deployment tasks.

Each task is represented as:

[taskName, prerequisites]

where:

taskName is a string representing the task.
prerequisites is a list of task names that must be completed before this task.
Every task name is unique.
A prerequisite will always refer to another task in the input.

getDeploymentOrder()

Returns a list containing all task names in a valid order of completion.

If multiple valid orders exist, return any valid order.

If it is impossible to complete all tasks because the dependencies contain a cycle, return an empty list.

Example 1
Input:
[
    ["Database Migration", []],
    ["Backend Deployment", ["Database Migration"]],
    ["Frontend Deployment", ["Backend Deployment"]],
    ["Smoke Tests", ["Frontend Deployment"]]
]

Output:
[
    "Database Migration",
    "Backend Deployment",
    "Frontend Deployment",
    "Smoke Tests"
]
Example 2
Input:
[
    ["Run Tests", ["Build"]],
    ["Build", ["Install Dependencies"]],
    ["Install Dependencies", []],
    ["Deploy", ["Run Tests"]]
]

Output:
[
    "Install Dependencies",
    "Build",
    "Run Tests",
    "Deploy"
]
Example 3
Input:
[
    ["Build", ["Test"]],
    ["Test", ["Build"]]
]

Output:
[]
Constraints
1 <= number of tasks <= 10^5
Each task has at most 10 prerequisites.
Task names contain only letters, numbers, spaces, and underscores.
The input may contain independent groups of tasks.
Your solution should handle the largest inputs efficiently.
'''
from collections import deque

class DeploymentManager:
    def __init__(self, tasks):
        self.graph = {}
        self.in_degree = {}

        for task, prereqs in tasks:
            self.graph[task] = []
            self.in_degree[task] = len(prereqs)

        for task, prereqs in tasks:
            for prereq in prereqs:
                self.graph[prereq].append(task)

    def getDeploymentOrder(self):
        queue = deque()

        for task in self.in_degree:
            if self.in_degree[task] == 0:
                queue.append(task)
            result = []

        while queue:
            task = queue.popleft()
            result.append(task)

            for next_task in self.graph[task]:
                self.in_degree[next_task] -= 1

                if self.in_degree[next_task] == 0:
                    queue.append(next_task)
        if len(result != len(self.graph)):
            return []
        return result



graph = {
    "Run Tests": ["Deploy"],
    "Build": ["Run Tests"],
    "Install Dependencies": ["Build"],
    "Deploy": [],
}

degree ={
    "Run Tests": 1,
        "Build": 1,
        "Install Dependencies": 0,
        "Deploy": 1,
}

"Install Dependencies", "Build", "Run Tests", "Deploy"

Output:
[
    "Install Dependencies",
    "Build",
    "Run Tests",
    "Deploy"
]