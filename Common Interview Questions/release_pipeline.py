'''
Release Pipeline

You are building an internal tool that manages the release process for a software product.

A release consists of several stages. Some stages cannot begin until other stages have been completed.

Implement a class called ReleaseManager.

Class Requirements

ReleaseManager(stages)

Initializes the system with a list of stages.

Each stage is represented as:

[stageName, dependencies]

where:

stageName is a unique string.
dependencies is a list of stage names that must be completed before this stage.
Every dependency refers to a stage in the input.

getReleaseOrder()

Returns a list containing all stages in an order that satisfies every dependency.

If multiple valid orders exist, return any valid order.

If there is no valid order because the dependencies contain a cycle, return an empty list.

Example 1
Input:
[
    ["Compile", []],
    ["Unit Tests", ["Compile"]],
    ["Build Image", ["Compile"]],
    ["Integration Tests", ["Build Image", "Unit Tests"]],
    ["Deploy", ["Integration Tests"]]
]

Output:
[
    "Compile",
    "Unit Tests",
    "Build Image",
    "Integration Tests",
    "Deploy"
]
Example 2
Input:
[
    ["Deploy", ["Security Scan"]],
    ["Security Scan", ["Build"]],
    ["Build", ["Compile"]],
    ["Compile", []]
]

Output:
[
    "Compile",
    "Build",
    "Security Scan",
    "Deploy"
]
Example 3
Input:
[
    ["Build", ["Test"]],
    ["Test", ["Deploy"]],
    ["Deploy", ["Build"]]
]

Output:
[]
Constraints
1 <= number of stages <= 100,000
Each stage has at most 20 dependencies.
Stage names are unique.
Dependencies may form multiple independent chains.
Return any valid ordering when one exists.
'''

from collections import deque

class ReleaseManager:
    def __init__(self, stages):
        self.store = {}
        self.degree = {}

        for stage, prereqs in stages:
            self.store[stage] = []
            self.degree[stage] = len(prereqs)

        for stage, prereqs in stages:
            for prereq in prereqs:
                self.store[prereq].append(stage)

    def getReleaseOrder(self):
        q = deque()
        for i in self.degree:
            if self.degree[i] == 0:
                q.append(i)
        result = []

        while q:
            stage = q.popleft()
            print(stage)
            for i in store[stage]:
                result.append(i)
                self.degree[i] -= 1

                if self.degree[i] == 0:
                    q.append(i)
        if len(result) != len(self.store):
            return []
        return result



store = ReleaseManager([
    ["Compile", []],
    ["Unit Tests", ["Compile"]],
    ["Build Image", ["Compile"]],
    ["Integration Tests", ["Build Image", "Unit Tests"]],
    ["Deploy", ["Integration Tests"]]
])
print(store.getReleaseOrder())